# TODO: Import the get_random_quote function from the api_handler file.
# import api_handler
from api_handler import get_random_quote

# TODO: Call the function and store the result in a variable named 'quote'.
quote = get_random_quote()

# Print the final quote
print("--- Your Inspirational Quote of the Day ---")
print(quote) # TODO: Uncomment this line after you've defined the 'quote' variable.

print("Log messages have been written to app.log")
