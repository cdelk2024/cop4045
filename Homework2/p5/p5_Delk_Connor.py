"""Weather-station observation analysis."""

import sys
from datetime import datetime


DATE_FORMAT = "%I:%M:%S %p %m/%d/%Y"
MIN_TEMPERATURE = -100.0
MAX_TEMPERATURE = 150.0


def read_observations(filename):
    """Read and validate weather observations from *filename*.

    Each valid input line has the form ``station,date,temperature``.  The
    returned dictionary maps station names to lists of ``(date, temperature)``
    tuples sorted chronologically.  Invalid lines are reported as
    ``(line_number, error_message)`` tuples.
    """
    observations = {}
    errors = []
    seen_station_dates = set()

    # Save parsed datetimes temporarily so sorting is chronological rather
    # than alphabetical.  They are removed before the result is returned.
    sortable_observations = {}

    with open(filename, "r", encoding="utf-8") as input_file:
        for line_number, line in enumerate(input_file, start=1):
            fields = line.strip().split(",")

            if len(fields) != 3:
                errors.append((line_number, "malformed line"))
                continue

            station, date, temperature_text = (field.strip() for field in fields)

            if not station or not date or not temperature_text:
                errors.append((line_number, "malformed line"))
                continue

            try:
                parsed_date = datetime.strptime(date, DATE_FORMAT)
            except ValueError:
                errors.append((line_number, "invalid date"))
                continue

            try:
                temperature = float(temperature_text)
            except ValueError:
                errors.append((line_number, "invalid temperature"))
                continue

            if not MIN_TEMPERATURE <= temperature <= MAX_TEMPERATURE:
                errors.append((line_number, "invalid temperature"))
                continue

            station_date = (station, parsed_date)
            if station_date in seen_station_dates:
                errors.append((line_number, "duplicate station/date"))
                continue

            seen_station_dates.add(station_date)
            sortable_observations.setdefault(station, []).append(
                (parsed_date, date, temperature)
            )

    for station, station_observations in sortable_observations.items():
        station_observations.sort(key=lambda observation: observation[0])
        observations[station] = [
            (date, temperature)
            for _, date, temperature in station_observations
        ]

    return observations, errors


def station_statistics(observations):
    """Return each station's minimum, maximum, and mean temperature.

    Each dictionary value is a ``(minimum, maximum, mean)`` tuple.
    """
    statistics = {}

    for station, station_observations in observations.items():
        temperatures = [
            temperature for _, temperature in station_observations
        ]

        if temperatures:
            statistics[station] = (
                min(temperatures),
                max(temperatures),
                sum(temperatures) / len(temperatures),
            )

    return statistics


def station_outliers(observations):
    """Return stations whose latest temperature exceeds their mean.

    Each returned value is a ``(date, temperature, mean)`` tuple.
    """
    statistics = station_statistics(observations)

    return {
        station: (
            station_observations[-1][0],
            station_observations[-1][1],
            statistics[station][2],
        )
        for station, station_observations in observations.items()
        if station_observations
        and station_observations[-1][1] > statistics[station][2]
    }


def write_statistics(filename, statistics):
    """Write station statistics to *filename* in lexicographic order.

    Output lines have the form ``station,minimum,maximum,mean``.
    """
    with open(filename, "w", encoding="utf-8") as output_file:
        for station in sorted(statistics):
            minimum, maximum, mean = statistics[station]
            output_file.write(
                f"{station},{minimum:.1f},{maximum:.1f},{mean:.1f}\n"
            )


def main():
    """Run the weather-station analyzer from the command line."""
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} input_file output_file")
        return

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    try:
        observations, errors = read_observations(input_filename)
        statistics = station_statistics(observations)
        outliers = station_outliers(observations)

        print("Errors:", errors)
        print("Statistics:", statistics)
        print("Outliers:", outliers)

        write_statistics(output_filename, statistics)
    except OSError as error:
        print(f"File access error: {error}")


if __name__ == "__main__":
    main()
