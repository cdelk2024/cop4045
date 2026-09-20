# Connor Delk
# Homework 2 Problem 1 

# This program creates a text file from the source code with each line numbered,
# and it finds the functions in the source code and returns information about each function 
# as a tuple 

def line_number(input_file: str, output_file: str) -> None:
    """Reads a text file and writes its numbered lines to a second text file"""
    # gives the file variables initial values 
    input_f = None
    output_f = None 
    
    try: 
        # opens original file for reading and new file for writing 
        input_f = open(input_file, "r")
        output_f = open(output_file, "w") 
        # ensures the line numbers for source code begin at 1 instead of zero 
        line_count = 1 
        # for loop to read through the original file 
        for text in input_f: 
            # writes the current line number, period, space, and original line 
            output_f.write("{}. {}".format(line_count, text))
            # increments line_count for next source line 
            line_count = line_count + 1 
        # Handle errors by printing a friendly message andf re-raising the original exception      
    except Exception as error:
        print("File was unable to be numbered: {}".format(error))
        raise
            
        # closes input file if it was successfully opened
    finally: 
        if input_f: 
            input_f.close()
          # closes output file if it was successfully opened   
        if output_f:
            output_f.close()
            
            
            
def parse_functions(filename: str) -> tuple: 
    """Parses functions from a .py file and returns their information""" 
    # assign initial value to file variable 
    input_f = None 
    
    try: # open the python file for reading
        input_f = open(filename, "r")
        # stores all lines in a list 
        lines = input_f.readlines() 
        # empty list to hold one tuple of info for each function 
        functions = []
        # comment character is character number 35, used to prevent mistakes when parsing # 
        comment_char = chr(35) 
        # for loop to iterate through every line in file
        for i in range(len(lines)):
            current = lines[i]
            # ensure the source file numbering begins at 1 instead of 0
            line_num = i + 1 
            # finds function definitions since they begin with "def " 
            if current.startswith("def "):
                # remove whitespace and newline so name and argument can be found 
                definition = current.strip() 
                # finds the parenthesis surrounding arguments 
                open_parenthesis = definition.find("(") 
                closed_parenthesis = definition.find(")")
                # function names begin after the "def " and before the open parenthesis
                # so index 4 is used along with open_parenthesis variable 
                function_name = definition[4:open_parenthesis]
                # arguments are located between open and closed parenthesis 
                arguments = definition[open_parenthesis + 1:closed_parenthesis] 
                # list to store the body lines and signature of function
                function_lines = []
                # begins collection at function definition 
                index = i
                # use while loop to continue until end of file or a non-indented statement is reached 
                while index < len(lines):
                    # retrieves the source code line at current index 
                    code_line = lines[index] 
                    # don't apply stopping test to original def line since it isnt indented 
                    if index > i : 
                        # examine the first character of a nonempty line since empty lines don't end a function 
                        if code_line.strip() != "": 
                            # obtains the first character of this line 
                            first_char = code_line[0]
                            # a body line in a function begins with a space or a tab 
                            # a comment can occur between two functions, it shouldn't end 
                            # collection
                            # if the line is not indented and is not a comment 
                            # it is a top-level statement. the current function will 
                            # then end before that line 
                            if first_char != " ":
                                if first_char != "\t": 
                                    if first_char != comment_char: 
                                        break 
                     # stores the current line as a possible part of the current function                
                    function_lines.append(code_line)
                    # advances to the next line 
                    index = index + 1 
                # combines the function lines into one string 
                function_code = "" 
                # for loop to examine every line collected for current function 
                for saved_line in function_lines: 
                    line_save = saved_line 
                    
                    # Remove the final newline using indexing and slicing 
                    if len(line_save)>0:
                        if line_save[-1] == "\n":
                            line_save = line_save[:-1]
                            
                    # ignore the empty lines 
                    if line_save.strip() != "":
                        # ignore the lines containing only a comment
                        if not line_save.strip().startswith(comment_char):
                            #find an inline comment
                            comment_pos = line_save.find(comment_char)
                            
                            # keep the code before the comment 
                            if comment_pos != -1: 
                                line_save = line_save[:comment_pos]
                                
                            # remove the spaces or tabs left before an inline 
                            # comment without removing the indentation 
                            while len(line_save) > 0:
                                last = line_save[-1]
                                
                                if ( last == " " or last == "\t"):
                                    line_save = line_save[:-1]
                                else: 
                                    break 
                            # add the remaining code if the line does not become empty 
                            if line_save.strip() != "":
                                function_code = (function_code + line_save + "\n")
                            
            # this is the required tuple with 4 elements 
            # function definition line number, function name, argument string, signature and body code string 
                function_info = (line_num, function_name, arguments, function_code) 
                # add the tuple to the list of functions 
                functions.append(function_info) 
                
          # alphabetize the collected tuples using function names 
          # outer loop selects one tuple position at a time 
        for first in range(len(functions)):
            # inner loop examines every tuple after the position selected by outer loop 
            for second in range(first + 1, len(functions)):
                # second element of tuple contains function name 
                name_1 = functions[first][1]
                name_2 = functions[second][1]
                # compare strings for alphabetical ordering 
                if name_2 < name_1: 
                    temp = functions[first]
                    functions[first] = functions[second]
                    functions[second] = temp 
         # converts the list of function tuples into outer tuple and returns                
        return tuple(functions) 
        # Handle errors by printing a friendly message andf re-raising the original exception      
    except Exception as error: 
        print("Python file could not be parsed: {}".format(error))
        raise 
       # closes the input file if it was opened successfully 
    finally: 
        if input_f: 
            input_f.close() 
        
            
        
def main() -> None: 
    """Main function that tests line_number function using source file"""
    input_filename = "p1_Delk_Connor.py" 
    # change output filename to ensure source code isn't wiped 
    output_filename = "p1_Delk_Connor_numbered.txt" 
    # call function line_number 
    line_number(input_filename, output_filename) 
    # print results 
    print("Numbered file was created") 
    print("Output file: {}".format(output_filename)) 
    # call function parsed_functions and store its returned tuple 
    parsed_functions = parse_functions(input_filename) 
    # display the returned tuple 
    print() 
    print("Parsed functions:")
    print(parsed_functions) 
    print() 
    print("Connor Delk") 
    
if __name__ == "__main__":
    main() 