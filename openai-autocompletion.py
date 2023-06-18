
# validate an email with regex and comment each line 
### at the end of the line press ctrl+shift+i

import re  # import regex library

# define regex pattern for email validation
pattern = r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"

# get the email from user input
email = input("Please enter your email: ")

# validate the email using regex pattern 
if re.match(pattern, email):  # if pattern matches with the given string 
    print("Valid Email")  # print valid message 
else:   # else print invalid message 
    print("Invalid Email")