# Connor Delk
# Homework 2 Problem 4 
# This program uses three CSV files and dictionaries to rank movie collaborations and earnings of actors 

import csv 

def load_casts(filename: str) -> dict: 
    """ Read the cast CSV file and return the contained movie information in a dictionary.""" 
    # Make an empty dictionary to store all of the cast information 
    casts = {} 
    # Make a variable for the file to assist with checking if the file opened successfully
    input_f = None 
    try: 
        # Open the casts file in read mode 
        input_f = open(filename, "r", encoding="utf-8", newline="") 
        # Connect CSV reader to input file 
        reader = csv.reader(input_f) 
        # Use for loop to read the CSV file one row at a time 
        for row in reader:
            # The first column has the movie title 
            title = row[0] 
            # The second column has the movie year
            year = row[1] 
            # The third column has the director of the movie 
            director = row[2] 
            # Every remaining column has actor names
            actors = row[3:] 
            # Title and year will be used together for dictionary key to 
            # help organize diferent movies with the same title 
            movie = (title, year) 
            # The director and actor list will be stored as the dictionary value 
            casts[movie] = (director, actors) 
            
        # Return the cast dictionary 
        return casts 
    # Display a friendly error message and re-raise the exception 
    except Exception as error:
        print("The cast file was unable to be loaded: {}".format(error))
        raise 
        
    finally: 
        # Close the file if it was successfully opened 
        if input_f:
            input_f.close() 
            
def load_movie(filename: str) -> dict:
    """ Read a CSV file with movie ranking and return the information inside
    the file in a dictionary""" 
    # Make an empty dictionary to store the information about the movies 
    movies = {} 
    # Make a variable for the file to assist with checking if the file opened successfully 
    input_f = None 
    try: 
        # Open the movie ranking file in read mode 
        input_f = open(filename, "r", encoding="utf-8", newline="") 
        # Connect CSV reader to input file 
        reader = csv.reader(input_f) 
        # Use for loop to read the CSV file one row at a time
        for row in reader:
            # The first row contains a header, so it needs to be skipped 
            if row[0] != "Rank":
                # The second column has the movie title
                title = row[1]
                # The third column has the movie year
                year = row[2] 
                # The fourth column has the rating or box-office amount
                value = row[3] 
                # The title and year will be the dictionary key like the previous function 
                movie = (title, year) 
                # The rating or box-office amount will be the dictionary value
                movies[movie] = value 
        # Returns the movie dictionary 
        return movies 
    
    except Exception as error: 
        # Displays a friendly message and re-raises the exception 
        print("The movie file could not be loaded: {}".format(error)) 
        raise 
        
    finally: 
        # Close the file if it was opened successfully 
        if input_f:
            input_f.close() 
            
# Part a 

def display_top_collaborations(casts: dict, rated_movies: dict, limit: int ) -> None: 
    """ Display top-rated movies for director and actor collaborations. """
    # Make a dictionary for counting each collaboration between director and actor
    collaborations = {} 
    # Use for loop to iterate through every movie in the top rated movie dictionary 
    for movie in rated_movies:
        # Get the director and actor list for the current movie from their respective indexes 
        director = casts[movie][0]
        actors = casts[movie][1]
        # Use a for loop to iterate through every actor in the movie 
        for actor in actors: 
            # The director and actor will be the dictionary key 
            pair = (director, actor) 
            # If the pair's count is already in the dictionary, increase its count 
            if pair in collaborations:
                collaborations[pair] += 1 
            # If not, begin the pair's count at one 
            else:
                collaborations[pair] = 1 
                
    # Make an empty list to be used for sorting by the collaboration count 
    rank = [] 
    # Use a for loop to add each collaboration to the rank list 
    for pair in collaborations: 
        # The count will be put first to help with sorting 
        rank.append((collaborations[pair], pair[0], pair[1])) 
        
    # Sort from greatest to least collaboration count 
    # Reverse since total was first
    rank.sort(reverse=True) 
    # When a positive limit is provided, cut the list 
    if limit > 0: 
        rank = rank[:limit]
    # use for loop to display each entry as director, actor, and number of movies 
    for entry in rank: 
        print((entry[1], entry[2], entry[0]))
        
# Part b         

def display_top_actors(casts: dict, grossing: dict, limit: int) -> None: 
    """ Displays actors ranked by total USA box-office earnings.""" 
    # Make a dictionary to store every eactors box-office earnings 
    totals = {} 
    # Use for loop to iterate through every movie in the top-grossing movie dictionary
    for movie in grossing:
        # Convert the box-office value from a string to an integer 
        box_value = int(grossing[movie])
        # Get the actor list for current movie
        actors = casts[movie][1] 
        # Use for loop to iterate through every actor in current movie
        for actor in actors:
            # If the actor is in the dictionary, add the box-office amount 
            if actor in totals:
                totals[actor] += box_value
                
            # Else, actor's total begins with this movie's box office value 
            else:
                totals[actor] = box_value 
                
    # Make a list to be sorted by box-office earnings 
    rank = []
    # Use for loop to add the actor and total to the rank 
    for actor in totals:
        # Place the total first to help with sorting 
        rank.append((totals[actor], actor))
        
    # Sort from greatest to least box-office total
    # Reverse since total was first 
    rank.sort(reverse=True)
    
    # When a positive limit is provided, cut the list 
    if limit > 0: 
        rank = rank[:limit]
    # Use for loop to display every result with the actor and box-office earnings 
    for entry in rank:
        print((entry[1], entry[0])) 
        
    
# Part c 

def main() -> None: 
    """ Load all movie data and test functions. """ 
    # Load the cast information into dictionary 
    casts = load_casts("imdb-top-casts.csv") 
    # Load the top-rated movie information into dictionary
    rated_movies = load_movie("imdb-top-rated.csv") 
    # Load the top-grossing movie information into dictionary
    grossing = load_movie("imdb-top-grossing.csv") 
    # Limit the rankings to the first ten entries 
    limit = 10 
    # Display all results from display_top_collaborations function from part a 
    print("Part a:") 
    print("Top director and actor collaborations:") 
    display_top_collaborations(casts, rated_movies, limit)
    # Blank line
    print() 
    # Display all results from display_top_actors function in part b 
    print("Part b:")
    print("Top actors by total box-office earnings:")
    display_top_actors(casts, grossing, limit)
    print()
    print("Connor Delk") 
    
    
if __name__ == "__main__":
    main() 
