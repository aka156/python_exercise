import requests
import logging

# logging.basicConfig(level=logging.DEBUG)

logging.basicConfig(filename='app.log', filemode='w', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
                    )
logger= logging.getLogger(__name__)

def get_random_quote():
    """Fetches a random quote from the quotable.io API."""
    try:
        response = requests.get("https://quotes-api-self.vercel.app/quote")
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()

        data = response.json()
        logger.debug(f"The response data: {data}")
        # print("data : ",data)
        quote = data['quote']
        author = data['author']
        logger.info(f'The author is:{author}')
        return f'"{quote}" - {author}'
    except requests.exceptions.RequestException as e:
     logger.error(f"Could not fetch the API")
     return f"Error: Could not fetch a quote. Please check your internet connection. Details: {e}"
        
# get_random_quote()