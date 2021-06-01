#              Author : Melvin M. Flores
#          Student ID : 30352985
#        Date Created : 29 April 2019
#        Program Name : AnagramTest.py
# Program Description : An anagram is a word or phrase formed by rearranging the letters of another
#                     : (e.g. "Listen; Silent", "Schoolmaster; The classroom", "Eleven Plus Two; Twelve Plus One", "Waitress; A Stew, Sir?").	
#                     : This program determines if the string is an anagram or not.
#          Input File : English.txt
#         Output File : Anagrams.txt
# Program Limitation  : The program considers a single character (e.g. "m", "F", "x") as NOT ANAGRAM.
#                     : Similarly, the program consider strings with numbers (e.g. "0", "5", "9") in it, as NOT ANAGRAM.
#                     : However, the program do consider strings with special characters (e.g. ",", "!", "'" ) in it by stripping it, 
#                     : and the remaining alphabetic characters are evauated if it is an anagram or not an anagram.

#imported for Counter object
from collections import Counter

#imported for file processing functions
import os

#imported for the set of alphabet and punctuation
import string

# Imported for determining execution time
import time

# Determine start of execution time
start_time = time.time()

# string set of punctuation
exclude = set(string.punctuation)      # used for the punctuation  set

# Opens the files for the first time
source = open("English.txt", "r")      # open input file
temp = open("EnglishSorted.txt", "w")  # open temporary input file for writing
dest = open("Anagrams.txt", "w")       # open output file

# Initialize counter values
AnagramCount = 0
NotAnagramCount = 0

# Function to remove formatting of the string, as well as sort the characters of the string
def unformat_string(formatted_string):
    unformatted_string = formatted_string.strip()             # removes unwanted WHITESPACES in the left and right side of the string
    unformatted_string = unformatted_string.lower()           # convert input string to lower case
    unformatted_string = unformatted_string.replace(' ','')   # replace SPACES with BLANK in the middle of the string
    
    unformatted_string = ''.join(ch for ch in unformatted_string if ch not in exclude)   # removes unwanted PUNCTUATIONS in the input string
    unformatted_string = unformatted_string.replace('\n','')  # replace NEWLINE ('\n) with BLANK in the right side of the string

    unformatted_string = sorted(unformatted_string)           # breaks the string into a list of sorted characters
    unformatted_string = ''.join(unformatted_string)          # bring it back to a string

    return unformatted_string                                 # returns unformatted string

# Read all the lines of the input file 
data = source.readlines()

# Sort all the lines of the input file
data.sort()

# Process each line in the input file 
for i in range(len(data)):
    input_string = data[i]                    # reads the string in the input file
    temp_str = unformat_string(input_string)  # calls the unformat_string function 

    # After stripping off all special characters, we are left with alphabetic or alphanumeric character
    # If temporary string is NOT ALPHABETIC, then skip the current string and proceed with the next string in the input file
    if (temp_str.isalpha() == False):
        continue                              # skip the current string and proceed with the next string in the input file loop 

    # If lengths of the string are either zero, one or two, then the string is not an anagram
    if (len(temp_str) == 0):     # length is zero,which means unformatted string has blank only
        continue                 # skip the current string and proceed with the next string in the input file loop

    if (len(temp_str) == 1):     # length is one, which means unformatted string has one character only
        continue                 # one character is not enough to be considered an anagram
                                 # skip the current string and proceed with the next string in the input file loop
                                  
    temp.write(temp_str + '\n')  # writes the unformatted and sorted string to a temporary input file

# Closes the files for the first time    
source.close()
temp.close()

# Opens the input files again 
source = open("English.txt", "r")      # open input file
temp = open("EnglishSorted.txt", "r")  # open newly created temporary input file, which has the unformatted and sorted string to be used for reading 

# Reads all lines of the input file
SourceLines = source.readlines()

# Counter for the number of lines of the input file
LineCountSource = len(SourceLines)

# Reads all lines of the temporary input file, which has the unformatted and sorted string
TempLines = temp.readlines()

# Used Counter object to count the frequency for each string of the temporary input file
ListCount = Counter(TempLines)

# Process each line in the input file
for key_loop in range(0,LineCountSource):          # reads key string in the key loop, from the input file
    original_string = SourceLines[key_loop]        # assign the key string to a variable for unformatting

    key_string = unformat_string(original_string)  # calls the unformat_string function, and assigns it to key string

    # After stripping off all special characters, we are left with alphabetic or alphanumeric character
    # If input string is NOT ALPHABETIC, then skip the current string and proceed with the next string in the input file
    if (key_string.isalpha() == False):
        continue                                   # skip the current string and proceed with the next string in the key loop 

    key_string = key_string + '\n'                 # adds NEWLINE ('\n) to the right side of the key string

    # Looks for the key string in the temporary sorted and unformatted input file which is the look-up string
    for ThisItem in ListCount.items():

        # If the key string is found in the look-up string and frequency of that string is greater than or equal to two,
        # which means that it found the string itself, and also found at the least it's anagram pair
        if key_string == ThisItem[0] and ThisItem[1] >= 2:
            AnagramCount += 1                      # increment counter for anagram
            dest.write(original_string)            # writes key string which is an anagram, to an output file
            break                                  # get out of the look-up loop since an anagram has been found
        
# Calculate for the counter of non-anagrams
NotAnagramCount = LineCountSource - AnagramCount

# Closes the input files again
source.close()
temp.close()

# Closes the output file
dest.close()

# Determine end of execution time
end_time = time.time()

# Calculate execution time
exec_time = end_time-start_time

# Summarizes the processing and displays the counters
print("Summary:")
print("  Total Strings in the \"English.txt\" input file : {:>7,}".format(LineCountSource))
print("                   Strings that are NOT ANAGRAM : {:>7,}".format(NotAnagramCount))
print("                       Strings that are ANAGRAM : {:>7,}\n".format(AnagramCount))
print("ALL ANAGRAM strings are listed in the \"Anagrams.txt\" output file\n")
print("Note:")
print("1. WHITESPACES and PUNCTUATIONS are REMOVED, and the remaining ALPHABETIC string is identified if it is ANAGRAM.")
print("2. Strings with NUMERIC DIGITS in it is considered as NOT ANAGRAM")
print("3. A single character (e.g. \'m\', \'F\', \'x\', and so on...) is not enough, and considered as NOT ANAGRAM")
print("\nExecution time : {:.2f} minutes".format(exec_time/60))

# Removes the temporary sorted and unformatted input file
os.remove("EnglishSorted.txt")
