import logging
import my_module  # Import the other file

# Configure logging for the entire application
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Get a logger for the main script
main_logger = logging.getLogger(__name__)

main_logger.info("Main application is starting.")
my_module.do_something() # Call the function from the other module
main_logger.info("Main application has finished.")

