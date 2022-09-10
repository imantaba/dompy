import os
from dotenv import load_dotenv

print(os.environ['HOME'])

# Use load_env to trace the path of .env:
load_dotenv('.env') 
 
# Get the values of the variables from .env using the os library:
password = os.environ.get("App_password")