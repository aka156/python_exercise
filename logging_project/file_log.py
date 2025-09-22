import logging

logging.basicConfig(filename='app.log', 
                    filemode='w', # w= write or overide and a=append and default is r=read
                    level=logging.INFO)

logging.info("The program started.")
logging.warning("An unusual event occurred.")
logging.info("The program is finishing.")

print("Log messages have been written to app.log")
