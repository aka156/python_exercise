import json
import logging

logging.basicConfig(filename='output.txt',
                    filemode='w',
                    level=logging.INFO)

# Read the JSON file in try/except block, parse it into a Python dictionary and log the dictionary variable

## Your code here

try:
    with open("order_data.json", 'r') as file:
        data=json.load(file)
    # print(data)
    logging.info("Data successfuly fetched")
    logging.info(f"parsed data:{data}")

except FileNotFoundError:
    logging.error("file not found")



# --- Accessing Nested Fields ---

# Access a top-level field "order_id" and log using info level
## Your code here
logging.info(f'Processing Order ID : {data['order_id']}')


# Access a field within a nested object, (customer --> name) and (customer -> address -> city). Log using info level
## Your code here
# logging.info(f"customer : {data['customer']}")
logging.info(f"customer: {data['customer']['name']} from {data['customer']['address']['city']}")


# --- Processing a Nested List ---
# Get total cost of the all the items and log the total billing amount
# print("\nOrder Items:")
total_cost =0
for i in data['items']:
    # print(i)
    logging.info(f"{i['product_name']} - ${i['price']}")
    total_cost += i['price']
logging.info(f"Total order cost: ${total_cost}")
    

