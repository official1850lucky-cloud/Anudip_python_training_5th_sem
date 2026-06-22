#write a program to allocate disaster relief resource
# Tasks 
# 1. Display all unique relief items.  
# 2. Find warehouses containing medicines.  
# 3. Count how many warehouses stock each resource.  
# 4. Identify the most widely available resource.  
# 5. Display resources available in all warehouses. 
#------------------------------------------------------
#create a sample data
resources = {
    "Warehouse1": ["Food", "Medicine", "Blankets"],
    "Warehouse2": ["Water", "Food", "Tents"],
    "Warehouse3": ["Medicine", "Tents", "Clothes"],
    "Warehouse4": ["Food", "Water", "Medicine"]
}
# 1. Display all unique relief items
unique_resources=[]
for items in resources.values():
    for item in items:
        if item not in unique_resources:
            unique_resources.append(item)
print("Unique Resources:")
print(unique_resources)
# 2. Find warehouses containing medicines
print("\nWarehouses with Medicines:")
for warehouse, items in resources.items():
    if "Medicine" in items:
        print(warehouse)
# 3. Count how many warehouses stock each resource
resource_count = {}
for items in resources.values():
    for item in items:
        if item in resource_count:
            resource_count[item] += 1
        else:
            resource_count[item] = 1
print("\nResource Availability:")
for resource, count in resource_count.items():
    print(resource, ":", count)
# 4. Identify the most widely available resource(s)
max_count = 0
for count in resource_count.values():
    if count > max_count:
        max_count = count
print("\nMost Widely Available Resources:")
for resource, count in resource_count.items():
    if count == max_count:
        print(resource)
# 5. Display resources available in all warehouses
common_resources = set(resources["Warehouse1"])
for items in resources.values():
    common_resources = common_resources.intersection(set(items))
print("\nResources Available in All Warehouses:")
if len(common_resources) == 0:
    print("None")
else:
    for item in common_resources:
        print(item)