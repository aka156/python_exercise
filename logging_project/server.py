# custom objects
import logging
logging.basicConfig(level=logging.INFO)
#create a list of server objects

class Server:
    """A custom object to represent a server with its key attributes."""
    def __init__(self, hostname: str, ip_address: str, status: str, cpu_usage: float, memory_usage: float):
        self.hostname = hostname
        self.ip_address = ip_address
        self.status = status
        self.cpu_usage = cpu_usage
        self.memory_usage = memory_usage

    def __repr__(self):
        """Provides a developer-friendly string representation of the object."""
        return (f"Server(hostname='{self.hostname}', ip='{self.ip_address}', "
                f"status='{self.status}', cpu={self.cpu_usage}%, mem={self.memory_usage}%)")
    
    def to_dict(self):
        """Converts the object's attributes to a dictionary."""
        return self.__dict__

servers = [
    Server("web-01","192.168.1.10","online",25.5, 45.0),
    Server("db-01", "192.168.1.11","offline", 0.0, 10.0),
    Server("app-01","192.168.1.12","online",85.0, 10.0),
    Server("cache-01", "192.168.1.13", "online",5.2, 22.8),
    Server("db-02","192.168.1.14","offline", 0.0, 10.0)          
]

#----Filtering-----
# use a list comprehension to find all offline servers
offline_servers = [s for s in servers if s.status == "offline"]
print("-----------Offline servers report-----")
# logging.info(offline_servers)
for server in offline_servers:
 logging.info(server)

# ------Sorting--------
#use the sorted() function with lambda key to sort by cpu usage in descending order
servers_sorted_by_cpu = sorted(servers, key=lambda s:s.cpu_usage, reverse= True)
print("\n---Servers sorted by cpu usage (high to low) ---")

for server in servers_sorted_by_cpu:
   logging.info(server)
logging.info(f"\nServer with highest cpu usage:{servers_sorted_by_cpu[0].hostname}")

print("---" *25)

#Exercise 2: Transforming Object data

servers = [
    Server("web-01", "192.168.1.10", "online", 25.5, 45.0),
    Server("db-01", "192.168.1.11", "offline", 0.0, 10.0),
    Server("app-01", "192.168.1.12", "online", 85.0, 60.5),
]

# Use a list comprehension to transform the data
inventory_report = [f"{s.hostname} ({s.ip_address})" for s in servers]

print("--- Network Inventory ---")
for entry in inventory_report:
    logging.info(entry)

print("\n")


# Exercise 3: Aggregating data from a list of objects

servers = [
    Server("web-01", "192.168.1.10", "online", 25.5, 45.0),
    Server("db-01", "192.168.1.11", "offline", 0.0, 10.0),
    Server("app-01", "192.168.1.12", "online", 85.0, 60.5),
    Server("cache-01", "192.168.1.13", "online", 5.2, 22.8),
]

online_servers = [s for s in servers if s.status =="online"] #this will get online servers only

if online_servers:
   cpu_usages = [s.cpu_usage for s in online_servers] # thsi will get cpu usage values
#    print(cpu_usages)

   average_cpu = sum(cpu_usages)/len(cpu_usages) # calculating avreage
#    print(average_cpu)

   print(f"---health summary for {len(online_servers)} online servers")
   logging.info(f"Average CPU usage: {average_cpu:.2f}%") # (.2f is for roundup the average from 38.56666666 t0 38.57%)
else:
   logging.info("No online servers found")

print("\n")



#Exercise 4: Building and Accessing a Server Dictionary
# Using the 'servers' list from Exercise 1

servers_list = [
    Server("web-01", "192.168.1.10", "online", 25.5, 45.0),
    Server("db-01", "192.168.1.11", "offline", 0.0, 10.0),
    Server("app-01", "192.168.1.12", "online", 85.0, 60.5),
]

servers_dict = {s.hostname: s for s in servers_list}
print("--------Server Dictionary-----")
logging.info(servers_dict)

#------fast lookup-----

target_hostname = "app-01"
if target_hostname in servers_dict:
    app_server = servers_dict[target_hostname]
    # print(app_server)
    print(f"\n--- Details for {target_hostname} ---")
    print(f"Status: {app_server.status}, CPU: {app_server.cpu_usage}%")
else:
    print(f"\nServer '{target_hostname}' not found.")

print("\n")

# Exercise 5: Updating Objects Within a Dictionary

# Using the 'servers_dict' from Exercise 4
servers_dict = {
    'web-01': Server(hostname='web-01', ip_address='192.168.1.10', status='online', cpu_usage=25.5, memory_usage=45.0),
    'db-01': Server(hostname='db-01', ip_address='192.168.1.11', status='offline', cpu_usage=0.0, memory_usage=10.0),
    'app-01': Server(hostname='app-01', ip_address='192.168.1.12', status='online', cpu_usage=85.0, memory_usage=60.5)
}

print(f"Status of web-01 before update: {servers_dict['web-01'].status}")

# --- Update the object's state ---
target_server = servers_dict.get("web-01")
# print(target_server)
if target_server:
    target_server.status = "offline"
    target_server.cpu_usage = 0.0
    print("Updated web-01 status.")

print(f"Status of web-01 after update: {servers_dict['web-01'].status}")
print(f"Full object after update: {servers_dict['web-01']}")


