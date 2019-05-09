import csv
# OpeN eXcEL 4 uR pRoJEct
# More categories: Office Supplies, Cosmetics, Snacks, Personal Care, Household, Baby Food, Vegetables, Cereal
with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    fruits_profit_list = []
    clothes_profit_list = []
    meat_profit_list = []
    beverages_profit_list = []
    for row in reader:
        region = row[0]
        category = row[2]
        profit = row[13]
        if category == "Fruits":
            print(region, category, profit)
            fruits_profit_list.append(float(profit))

        if category == "Clothes":
            print(region, category, profit)
            clothes_profit_list.append(float(profit))

        if category == "Meat":
            print(region, category, profit)
            meat_profit_list.append(float(profit))

        if category == "Beverages":
            print(region, category, profit)
            beverages_profit_list.append(float(profit))


fruits_sum = sum(fruits_profit_list)
clothes_sum = sum(clothes_profit_list)
meat_sum = sum(meat_profit_list)
beverages_sum = sum(beverages_profit_list)
print("The total profit for the Fruits category is %f" % fruits_sum)
print("The total profit for the Clothes category is %f" % clothes_sum)
print("The total profit for the Meat category is %f" % meat_sum)
print("The total profit for the Beverages category is %f" % beverages_sum)
