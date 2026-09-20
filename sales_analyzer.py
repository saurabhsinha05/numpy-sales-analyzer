```python
import numpy as np

sales = np.array([
    [1200, 1500, 1100, 1800, 1400],   # Monday
    [1600, 1300, 1700, 1900, 1500],   # Tuesday
    [1000, 1200, 1400, 1300, 1100],   # Wednesday
    [1800, 1700, 1600, 2000, 1900],   # Thursday
    [1400, 1600, 1500, 1700, 1800]    # Friday
])

products = ["Milk", "Bread", "Rice", "Oil", "Snacks"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


# Total sales of every day
total = np.sum(sales, axis=1)

for i in range(len(days)):
    print("Sales on", days[i], "is", total[i])

print("-" * 40)


# Total sales of every product
total_product = np.sum(sales, axis=0)

for i in range(len(products)):
    print("Sales of", products[i], "is", total_product[i])

print("-" * 40)


# Average sales of every day
average = np.mean(sales, axis=1)

for i in range(len(days)):
    print("Average sale on", days[i], "is", average[i])

print("-" * 40)


# Day with highest sales
print("Highest sale is on", days[np.argmax(total)])

print("-" * 40)


# Highest selling product
print("Highest sold product is:", products[np.argmax(total_product)])

print("-" * 40)


# Days with sales more than 7000
for i in range(len(days)):
    if total[i] > 7000:
        print("Sale more than 7000 is on:", days[i], "that is", total[i])

print("-" * 40)


# Total sales
print("Total sales:", np.sum(sales))

print("-" * 40)


# Percentage contribution of every product
for i in range(len(products)):
    percentage = (total_product[i] / np.sum(total)) * 100
    print("Percentage of", products[i], "is:", int(percentage))

print("-" * 40)


# Classifying each day based on sales
for i in range(len(days)):
    if total[i] >= 7500:
        print(days[i], ": Excellent")
    elif total[i] >= 6500:
        print(days[i], ": Good")
    elif total[i] >= 5500:
        print(days[i], ": Average")
    else:
        print(days[i], ": Low")

print("-" * 40)
```
