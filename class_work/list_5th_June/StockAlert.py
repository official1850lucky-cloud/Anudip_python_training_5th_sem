# wap to display out of stock, restocking, available products in iventory stock alert system
stock = [25, 5, 0, 12, 3, 18, 0, 30] 
out_of_stock_count = 0
restock_required = []
available_products_count = 0
healthy_stock = []
# loop for stock
for s in stock:
    # Out of stock products (quantity == 0) 
    if s == 0:
        out_of_stock_count += 1
    #Restocking required (quantity < 10) 
    if s < 10:
        restock_required.append(s)   
    #Available products (stock > 0)
    if s > 0:
        available_products_count += 1
    # Stock greater than or equal to 15 
    if s >= 15:
        healthy_stock.append(s)
# Outputs print karte hain
print("Out of Stock Products:", out_of_stock_count) 
print("Restock Required:", restock_required) 
print("Available Products:", available_products_count) 
print("Healthy Stock:", healthy_stock)