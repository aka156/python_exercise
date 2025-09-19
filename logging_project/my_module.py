import logging

# Get a logger for this specific module
module_logger = logging.getLogger(__name__)

def do_something():
    module_logger.info("Doing something in my_module!")
