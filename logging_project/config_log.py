import logging

# Configure the logging system
# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)

logging.debug("This message will NOT be shown, because the level is INFO.")
logging.info("This message WILL now be shown.")
logging.warning("This one will also be shown.")
