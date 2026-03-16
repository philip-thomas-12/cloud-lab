import pandas as pd
from itertools import combinations



data = pd.read_csv("data6.csv")

min_support = 0.4

transactions = []

for i in range(len(data)):
    transaction = []
    for item in data.columns:
        if data.loc[i, item] == 1:
            transaction.append(item)
    transactions.append(transaction)

items = list(data.columns)

frequent_itemsets = []

for i in range(1, len(items) + 1):
    for combo in combinations(items, i):
        count = 0
        for transaction in transactions:
            if set(combo).issubset(set(transaction)):
                count += 1

        support = count / len(transactions)

        if support >= min_support:
            frequent_itemsets.append((combo, support))

print("Frequent Itemsets:")

for itemset in frequent_itemsets:
    print(itemset)

