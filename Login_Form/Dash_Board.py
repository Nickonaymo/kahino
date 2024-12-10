import matplotlib.pyplot as plt

PRICES = {
    "burgers": {
        "Classic Burger": 120,
        "Veggie Burger": 130,
        "Cheesy Burger": 140,
        "Cheesy Bacon Burger": 150,
        "Ultimate Burger": 160,
    },
    "fries": {
        "Small Fries": 47,
        "Medium Fries": 65,
        "Large Fries": 80,
    },
    "drinks": {
        "Coffee": 50,
        "Hot Choco": 60,
        "Iced Tea": 40,
        "Juice": 45,
        "Soft Drinks": 35,
    },
    "pizza": {
        "Ham and Cheese Pizza": 200,
        "Pepperoni Pizza": 220,
        "Hawaiian Pizza": 210,
        "Cheese Pizza": 190,
        "Veggie Pizza": 230,
    }
}

# Updated color palette to match #ee7304
plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#ee7304", "#ff9d56", "#ffca8b", "#fac68e", "#f7e2cb"]
)

# Flatten the nested dictionary
items = []
prices = []

for category, products in PRICES.items():
    for product, price in products.items():
        items.append(product)
        prices.append(price)

# Chart: Bar Chart of Sales
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(items, prices, color=plt.rcParams["axes.prop_cycle"].by_key()["color"])

# Rotate item names for better readability
ax.set_xticklabels(items, rotation=90, ha="right", fontsize=10)
ax.set_xlabel('Items', fontsize=12)
ax.set_ylabel('Price (in currency)', fontsize=12)
ax.set_title('Food Item Prices', fontsize=14, color="#ee7304")

# Add data labels
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 5, f'{yval}', ha='center', fontsize=10)

plt.tight_layout()  # Adjust layout for better fitting
plt.show()
