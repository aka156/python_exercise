import logging

# Configure logging with a custom format
logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("This is a formatted info message.")
logging.error("This is a formatted error message.")
