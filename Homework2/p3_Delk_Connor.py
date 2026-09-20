# Connor Delk
# Homework 2 Problem 3 

import csv 
from testif import testif 
# Part a 

def add_user(sn: dict, username: str, fullname: str) -> bool: 
    """ Adds a new user to a social network. Returns True if the user is successfully
    added and returns False if the username already exists in the network. """ 
    
    try: 
        # If username already exists, return False 
        if username in sn:
            return False 
        # Add the username as a key. The value is a tuple that contains the user's 
        # full name and an empty friend list 
        sn[username] = (fullname, []) 
        # The user was successfully added and function returns True 
        return True 
    # Handle errors by printing a friendly message and re-raising the exception 
    except Exception as error: 
        print("The user was unable to be added: {}".format(error))
        raise 

# Part b 

def add_friend(sn: dict, user1: str, user2: str) -> bool: 
    """ Create friendship between two users in social network. 
    Return True if both users exist and the friendship is added successfully. 
    Return False if either username is missing. """ 
    
    try: 
        # Both usernames must exist in the network 
        if user1 not in sn or user2 not in sn: 
            return False 
        # Username structure (full_name, friends_list) 
        # Add user1's name to user2's friends list 
        if user1 not in sn[user2][1]:
            sn[user2][1].append(user1) 
        # Add user 2's name to user1's friends list 
        if user2 not in sn[user1][1]:
            sn[user1][1].append(user2)
        
        return True 
    # Handle errors by printing a friendly message and re-raising the exception
    except Exception as error: 
        print("The friend could not be added: {}".format(error))
        raise 
        
        
# Part c 
     
def get_friends(sn: dict, user1: str, distance: int) -> list: 
    """ Return all friends that are reachable from a user within the given distance. 
    Return an empty list if the username is missing or there are no friends available. """ 
    
    try: 
        # If username is missing, no friend is returned 
        if user1 not in sn:
            return []
        # If distance is not a positive integer >0, there are no friendship links 
        if distance <= 0: 
            return []
        # Empty list to store every friend that is returned 
        found = [] 
        # A visited list to keep track of all visited user to prevent any duplicates
        # The starting user has already been visited, so must not be returned as their own friend 
        visited = [user1] 
        # List of users at the current distance level
        level_current= [user1] 
        # The starting user will be at 0 distance
        distance_current = 0 
        # Use while loop to search until requested distance has been examined 
        while distance_current < distance:
            # Store users found at next distance level in an empty set 
            level_next = [] 
            # For loop to visit every user at the current distance level 
            for current_user in level_current: 
                # for loop to access the current user's friend list 
                # First index of the user's tuple is what contains that list 
                for friend in sn[current_user][1]:
                    # Successfully process friend only if friend has not been encountered
                    if friend not in visited: 
                        # Append friend to visited to ensure htey cannot be added again
                        visited.append(friend) 
                        # Add friend to final result 
                        found.append(friend) 
                        # Add the friend to next level so their list can be examined 
                        # if the distance requested allows for another iteration 
                        level_next.append(friend) 
            
            # Users that are found during this iteration will become 
            # the user that are examined during the next 
            level_current = level_next 
            # A complete friendship level has been examined 
            distance_current = distance_current + 1 
            # Stop the loop if no new users are found 
            if len(level_current) == 0:
                break 
            
        # Return all of the unique friends found from distance 1 through the maximum 
        return found 
    # Displays a friendly message and re-raises the exception 
    except Exception as error: 
        print("Friends could not be found: {}".format(error)) 
        raise 
        
# Part d 

def save_network(filename: str, sn: dict) -> None: 
    """ Function saves a social-network dictionary to a CSV file. 
    Each row in the CSV file contains a username, the user's full name, and all 
    usernames in that user's friend list. """
    # Giving the file variable an initial value so the finally block of the try except 
    # can determine if the file was opened successfully 
    output_f = None 
    
    try: 
        # Open the CSV file in write mode, use newline="" to prevent blank rows 
        output_f = open(filename, "w", newline="") 
        # Create CSV writer which connects to the output file 
        writer = csv.writer(output_f) 
        
        # Use for loop to visit each username stored as a key in network 
        for username in sn: 
            # The user's full name is contained in index 0
            full_name = sn[username][0] 
            # The user's friend list is contained in index 1 
            friend_list = sn[username][1] 
            # Make the CSV row begin with the username and full name 
            row = [username, full_name] 
            # Use for loop to add every friend's username to the end of row
            for friend in friend_list:
                row.append(friend) 
            # Write completed list as one row in the file 
            writer.writerow(row) 
    # Displays a friendly message and re-raises the exception 
    except Exception as error:
        print("The social network can't be saved: {}".format(error))
        raise 
    
    finally: 
        # Close output file if it was opened 
        if output_f:
            output_f.close() 

     
        
# Part e 

def load_network(filename: str) -> dict: 
    """ Function to read a social network from a CSV file and return its dictionary. 
    Each row of the CSV file contains a username, full name, and zero or more friends username""" 
    # File variable gets an initial value so it can be checked if the file opens successfully
    input_f = None 
    
    try: 
        # Open the file in read mode and use newline="" to prevent blank rows 
        input_f = open(filename, "r", newline="") 
        # Create CSV reader which connects to the input file 
        reader = csv.reader(input_f) 
        # Dictionary that will hold the network 
        network = {} 
        # Use a for loop to read one row of the CSV file at a time 
        for row in reader: 
            # The first index contains the username
            username = row[0] 
            # The second index contains the full name of the user 
            full_name = row[1] 
            # The fields that remain all contain friend usernames 
            friend_list = row[2:] 
            # Recreate the dictionary using the tuple which contains the full name and friend list 
            network[username] = (full_name, friend_list) 
        # Return the recreated social network dictionary
        return network 
    
    #Display a friendly message and re-raise the exception if the file is unable to be 
    # opened or read 
    except Exception as error:
        print("The social network cannot be loaded: {}".format(error))
        raise 
        
    finally: 
        # Close the input file if it was successfully opened 
        if input_f: 
            input_f.close() 
            
            
# Part f 

def main() -> None: 
    """ Main function that creates a sample social network and tests every function.""" 
    try: 
        # Create an empty dictionary to be used for the social network 
        sn = {} 
        # Test function calls to the add_user function 
        print("Test add_user function:") 
        print(add_user(sn, "alice", "Alice Smith"))
        print(add_user(sn, "maria", "Maria Cortez")) 
        print(add_user(sn, "joe", "Joseph Adams"))
        print(add_user(sn, "eve", "Evelyn Cooper")) 
        print(add_user(sn, "david", "David Benson")) 
        
        # Test add_user function with a username that already exists
        print()
        print("Testing duplicate username:")
        print(add_user(sn, "alice", "Different")) 
        
        # Display the social network before adding friendships 
        print() 
        print("Network before friendships:")
        print(sn) 
        
        # Test function calls to add_friend function 
        print() 
        print("Test add_friend function:")
        print(add_friend(sn, "alice", "maria"))
        print(add_friend(sn, "maria", "joe")) 
        print(add_friend(sn, "joe", "eve"))
        print(add_friend(sn, "maria", "david"))
        
        # Test friendship with a missing username 
        print() 
        print("Test add_friend with missing username:")
        print(add_friend(sn, "alice", "michael"))
        
        # Test add_friend for existing friendship
        print()
        print("Testing add_friend with an existing frienship:")
        print(add_friend(sn, "alice", "maria")) 
        
        # Display complete network
        print()
        print("Complete network:")
        print(sn)
        
        # Test get_friends function at distance 1 
        print() 
        print("Alice's friends from distance 1:")
        print(get_friends(sn, "alice", 1))
        
        # Test get_friends function at distance 2 
        print() 
        print("Alice's friends from distance 2:")
        print(get_friends(sn, "alice", 2))
        
        # Test get_friends function at distance 3
        print()
        print("Alice's friends from distance 3:")
        print(get_friends(sn, "alice", 3)) 
        
        #Test get_friends with nonexistant username 
        print() 
        print("Test get_friend function with nonexistant username:")
        print(get_friends(sn, "michael", 2)) 
        
        print("Connor Delk") 
        
        
        # Store name of CSV file in variable for saving and loading file 
        csv_filename = "social_network.scv"
        
        # Test save_network function by writing current dictionary to file 
        print()
        print("Saving social network:")
        save_network(csv_filename, sn)
        print("The social network was successfully saved.") 
        
        # Test load_network function by recreating new dictionary from the CSV file 
        print()
        print("Loading social network:")
        loaded_network = load_network(csv_filename)
        print(loaded_network) 
        
        # Confirm loaded netowrk can still be searched 
        print() 
        print("Alice's loaded friends from distance 2:")
        print(get_friends(loaded_network, "alice", 2))
        
    # Display a friendly essage and re-raise the exception
    except Exception as error: 
        print("The social network test was unable to be completed: {}".format(error))
        raise 
        
# Part g 

def test() -> None: 
    """Test all functions for parts a-e using testif.""" 
    # Make an empty network used for these tests 
    test_sn = {} 
    # Test add_user function by adding 5 sample users
    testif(add_user(test_sn, "alice", "Alice Smith") == True, "add_user successfully adds Alice") 
    testif(add_user(test_sn, "maria", "Maria Cortez") == True, "add_user successfully adds Maria") 
    testif(add_user(test_sn, "joe", "Joseph Adams") == True, "add_user successfully adds Joe") 
    testif(add_user(test_sn, "eve", "Evelyn Cooper") == True, "add_user successfully adds Eve") 
    testif(add_user(test_sn, "david", "David Benson") == True, "add_user successfully adds David") 
    #Test that the add_user function returns False for a duplicate username 
    testif(add_user(test_sn, "alice", "Different") == False, "add_user successfully rejects a duplicate username")
    # Test the add_friend function by adding each friendship from the sample network
    testif(add_friend(test_sn, "alice", "maria") == True, "add_friend successfully connects Alice and Maria")
    testif(add_friend(test_sn, "maria", "joe") == True, "add_friend successfully connects Maria and Joe")
    testif(add_friend(test_sn, "joe", "eve") == True, "add_friend successfully connects Joe and Eve")
    testif(add_friend(test_sn, "maria", "david") == True, "add_friend successfully connects Maria and David") 
    # Confirm friendship between Alice and Maria is mutual
    testif("maria" in test_sn["alice"][1] and "alice" in test_sn["maria"][1], "add_friend successfully creates a mutual friendship") 
    # Test that the add_friend function returns False when a username is missing 
    testif(add_friend(test_sn, "alice", "michael") == False, "add_friend successfully rejects a missing username") 
    # Test the get_friends function at distance 1 
    testif(get_friends(test_sn, "alice", 1) == ["maria"], "get_friends sucessfully returns Alice's friends at distance 1")
    # Test the get_friends function from distance 2 
    testif(get_friends(test_sn, "alice", 2) == ["maria", "joe", "david"], "get_friends successfully returns Alice's friends from distance 2")
    # Test the get_friends function from distance 3 
    testif(get_friends(test_sn, "alice", 3) == ["maria", "joe", "david", "eve"], "get_friends successfully returns Alice's from distance 3")
    #Test the get_friends function with a missing username that should produce an empty list 
    testif(get_friends(test_sn, "michael", 2) == [], "get_friends successfully handled a missing username") 
    # Create variable to store name of CSV test file 
    test_filename = "test_social_network.csv" 
    
    try: 
        # Test the save_network function by apptempting to save the test dictionary 
        save_network(test_filename, test_sn)
        # If this line of code is successfully reached, then the file saved without exception 
        testif(True, "save_network successfully saves the social network")
        # Test the load_network function by loading the CSV file
        loaded_sn = load_network(test_filename)
        # The loaded dictionary should be equal to the original dictionary 
        testif(loaded_sn == test_sn, "load_network successfully recreates the saved social network") 
        
    except Exception: 
        # A file exception occurs when the save or load test fails 
        testif(False, "save_network and _load_network") 
    
if __name__ == "__main__":
    main() 
    
    
    print()
    print("Part g testif module tests:") 
    test() 
    print("Connor Delk") 
    

            