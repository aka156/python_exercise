import requests


def get_random_quote():
    """Fetches a random quote from the quotable.io API."""
    try:
        response = requests.get("https://quotes-api-self.vercel.app/quote")
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()

        data = response.json()
        # print("data : ",data)
        quote = data['quote']
        author = data['author']
        return f'"{quote}" - {author}'
    except requests.exceptions.RequestException as e:
     return f"Error: Could not fetch a quote. Please check your internet connection. Details: {e}"
        

get_random_quote()