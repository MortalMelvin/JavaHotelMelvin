#              Author : Melvin M. Flores
#          Student ID : 30352985
#        Date Created : 27 April 2019
#        Program Name : PalindromeTest.py
# Program Description : A palindrome is a word or phrase that reads the same backwards or forwards
#                     : (e.g. "kayak", "Never odd or even", "Madam, I'm Adam!").	
#                     : This program determines if the string is a palindrome or not.
#          Input File : English.txt
#         Output File : Palindromes.txt
# Program Limitation  : The program do not consider strings with numbers (e.g. "0", "5", "9") in it, thus it is not evaluated.
#                     : However, the program do consider strings with special characters (e.g. ",", "!", "'" ) in it.
#                     : Also, the program considers a single character (e.g. "m", "F", "x") as a palindome.

# imported for the punctuation and digits set
import string


# string set of punctuation
exclude = set(string.punctuation)       # used for the punctuation  set

# Opens the fies
source = open("English.txt", "r")       # open  input file
dest   = open("Palindromes.txt", "w")   # open output file

# Initialize counter values
StringCount = 0
PalindromeCount = 0
NotPalindromeCount = 0

# Process each line in the input file
for line in source:                                          # read each string in the input file
        
    original_string = line                                   # assign the string read from the input file to a variable

    # Removes formatting of the string
    unformatted_string = original_string.strip()             # remove unwanted WHITESPACES in the left and right side of the input string
    unformatted_string = unformatted_string.lower()          # convert input string to lower case
    unformatted_string = unformatted_string.replace(' ','')  # replace SPACES with BLANK in the middle of the input string

    unformatted_string = ''.join(ch for ch in unformatted_string if ch not in exclude)   # removes unwanted PUNCTUATIONS in the input string

    # After stripping off all special characters, we are left with alphabetic or alphanumeric character
    # If input string is NOT ALPHABETIC, then skip the current string and proceed with the next string in the input file
    if (unformatted_string.isalpha() == False):
        NotPalindromeCount += 1				    # increment counter for Not Palindrome
        StringCount += 1                                    # increment counter for input string
        continue
    
    reverse_string = unformatted_string[::-1]               # reverses the unformatted input string

    if len(unformatted_string) == 0:                        # everything are removed, no more characters left to process
        NotPalindromeCount += 1			            # increment counter for Not Palindrome
    elif unformatted_string == reverse_string:              # compares the unformatted input string with the reversed input string
        PalindromeCount += 1                                # increment counter for Palindrome
        dest.write(line)                                    # write Palindrome string in output file
    else:
        NotPalindromeCount += 1                             # increment counter for Not Palindrome
        
    StringCount += 1                                        # increment counter for input string
    
# Closes the fies
source.close()
dest.close()

# Summarizes the processing and displays the counters
print("Summary:")
print("  Total Strings in the \"English.txt\" input file : {:>7,}".format(StringCount))
print("                Strings that are NOT PALINDROME : {:>7,}".format(NotPalindromeCount))
print("                    Strings that are PALINDROME : {:>7,}\n".format(PalindromeCount))
print("ALL PALINDROME strings are listed in the \"Palindromes.txt\" output file\n")
print("Notes:")
print("1. WHITESPACES and PUNCTUATIONS are REMOVED, and the remaining ALPHABETIC string is identified if it is a PALINDROME.")
print("2. Strings with NUMERIC DIGITS in it is considered as a NOT PALINDROME")
print("3. A single character (e.g. \'m\', \'F\', \'x\', and so on...) is considered as a PALINDROME.")
