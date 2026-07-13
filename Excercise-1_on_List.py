# ExCERCISE 1: Managing an Inventory

# 1. Creation & Appending: Create an empty list named inventory. Add the following items to the end of the list one by one using .append(): "apples", "bananas", "carrots".

# 2. Inserting: You realize you need a high-priority item at the very front of your list. Insert "milk" at index 0.

# Extending: A delivery truck arrives with a batch of new items: ["eggs", "bread", "cheese"]. Use .extend() to add these to your current inventory.

# 4. Slicing: Create a new list called aisle_one that contains only the first 3 items currently in your inventory.

# 5. Removal & Popping: Someone bought the last bag of carrots. Remove "carrots" from the inventory by its value.

# You need to audit the very last item in your list. Use .pop() to remove the last item from the inventory and store it in a variable called audited_item.

# 6. List Comprehension: You have a list of item prices: prices = [10, 15, 23, 42, 55]. Use a list comprehension to create a new list called sale_prices that keeps only the prices that are greater than 20.

# 7. Functions & Sorting: Using your sale_prices list:

# A.Print the total sum of the sale prices.

# B.Sort the sale_prices list in descending order (highest to lowest) and print it.

# 1. Creation & Appending
inventory = []

inventory.append("apples")
inventory.append("bananas")
inventory.append("carrots")

print("Inventory after appending:", inventory)

# 2. Inserting
inventory.insert(0, "milk")

print("Inventory after inserting milk:", inventory)

# 3. Extending
inventory.extend(["eggs", "bread", "cheese"])

print("Inventory after extending:", inventory)

# 4. Slicing
aisle_one = inventory[:3]

print("Aisle One:", aisle_one)

# 5. Removal & Popping
inventory.remove("carrots")

audited_item = inventory.pop()

print("Inventory after removing carrots:", inventory)
print("Audited Item:", audited_item)

# 6. List Comprehension
prices = [10, 15, 23, 42, 55]
