"""Unit tests for the weather-station analyzer."""

import os
import tempfile
import unittest

from p5_Delk_Connor import (
    read_observations,
    station_outliers,
    station_statistics,
    write_statistics,
)


class WeatherStationTests(unittest.TestCase):
    """Tests for reading, analyzing, and writing weather observations."""

    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.temporary_directory.cleanup()

    def make_input_file(self, contents):
        """Create and return the path to a temporary input file."""
        filename = os.path.join(self.temporary_directory.name, "observations.txt")
        with open(filename, "w", encoding="utf-8") as test_file:
            test_file.write(contents)
        return filename

    def test_reads_several_stations(self):
        filename = self.make_input_file(
            "Miami,09:00:00 AM 04/20/2026,81.0\n"
            "Orlando,10:30:00 AM 04/20/2026,78.5\n"
            "Tampa,11:15:00 AM 04/20/2026,79.0\n"
        )

        observations, errors = read_observations(filename)

        self.assertEqual(set(observations), {"Miami", "Orlando", "Tampa"})
        self.assertEqual(errors, [])

    def test_accepts_negative_and_boundary_temperatures(self):
        filename = self.make_input_file(
            "North,09:00:00 AM 01/01/2026,-25.5\n"
            "North,10:00:00 AM 01/01/2026,-100.0\n"
            "South,11:00:00 AM 01/01/2026,150.0\n"
        )

        observations, errors = read_observations(filename)

        self.assertEqual(errors, [])
        self.assertEqual(observations["North"][0][1], -25.5)
        self.assertEqual(observations["North"][1][1], -100.0)
        self.assertEqual(observations["South"][0][1], 150.0)

    def test_rejects_duplicate_observations(self):
        filename = self.make_input_file(
            "Miami,09:00:00 AM 04/20/2026,80.0\n"
            "Miami,09:00:00 AM 04/20/2026,82.0\n"
        )

        observations, errors = read_observations(filename)

        self.assertEqual(
            observations,
            {"Miami": [("09:00:00 AM 04/20/2026", 80.0)]},
        )
        self.assertEqual(errors, [(2, "duplicate station/date")])

    def test_rejects_invalid_temperature_ranges(self):
        filename = self.make_input_file(
            "Cold,09:00:00 AM 04/20/2026,-100.1\n"
            "Hot,10:00:00 AM 04/20/2026,150.1\n"
            "Broken,11:00:00 AM 04/20/2026,warm\n"
        )

        observations, errors = read_observations(filename)

        self.assertEqual(observations, {})
        self.assertEqual(
            errors,
            [
                (1, "invalid temperature"),
                (2, "invalid temperature"),
                (3, "invalid temperature"),
            ],
        )

    def test_calculates_station_statistics(self):
        observations = {
            "Miami": [("date 1", 70.0), ("date 2", 80.0), ("date 3", 90.0)],
            "Tampa": [("date 1", -10.0), ("date 2", 20.0)],
        }

        statistics = station_statistics(observations)

        self.assertEqual(statistics["Miami"], (70.0, 90.0, 80.0))
        self.assertEqual(statistics["Tampa"], (-10.0, 20.0, 5.0))

    def test_finds_station_outliers(self):
        observations = {
            "Miami": [("date 1", 70.0), ("date 2", 90.0)],
            "Tampa": [("date 1", 90.0), ("date 2", 70.0)],
        }

        self.assertEqual(
            station_outliers(observations),
            {"Miami": ("date 2", 90.0, 80.0)},
        )

    def test_observations_and_output_are_sorted(self):
        filename = self.make_input_file(
            "Zulu,01:00:00 PM 04/21/2026,75.0\n"
            "Alpha,09:00:00 AM 04/20/2026,60.0\n"
            "Zulu,08:00:00 AM 04/20/2026,65.0\n"
        )
        observations, _ = read_observations(filename)
        self.assertEqual(observations["Zulu"][0][1], 65.0)

        output_filename = os.path.join(
            self.temporary_directory.name, "statistics.txt"
        )
        write_statistics(
            output_filename,
            {"Zulu": (65.0, 75.0, 70.0), "Alpha": (60.0, 60.0, 60.0)},
        )

        with open(output_filename, "r", encoding="utf-8") as output_file:
            self.assertEqual(
                output_file.read(),
                "Alpha,60.0,60.0,60.0\nZulu,65.0,75.0,70.0\n",
            )

    def test_missing_file_raises_file_not_found_error(self):
        missing_filename = os.path.join(
            self.temporary_directory.name, "missing.txt"
        )

        with self.assertRaises(FileNotFoundError):
            read_observations(missing_filename)


if __name__ == "__main__":
    unittest.main()
