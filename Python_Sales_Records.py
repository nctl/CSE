import csv

# What is the product with the highest profit margin per unit?

with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    fruits_profit_list = []
    clothes_profit_list = []
    meat_profit_list = []
    beverages_profit_list = []
    office_supplies_profit_list = []
    cosmetics_profit_list = []
    snacks_profit_list = []
    personal_care_profit_list = []
    household_profit_list = []
    baby_food_profit_list = []
    vegetables_profit_list = []
    cereal_profit_list = []

    sub_saharan_africa_profit_list = []
    mideast_and_north_africa_profit_list = []
    oceania_profit_list = []
    europe_profit_list = []
    asia_profit_list = []
    c_america_and_caribbean_profit_list = []
    n_america_profit_list = []
    for row in reader:
        region = row[0]
        category = row[2]
        profit = row[13]
        if category == "Fruits":
            #  print(region, category, profit)
            fruits_profit_list.append(float(profit))

        if category == "Clothes":
            #  print(region, category, profit)
            clothes_profit_list.append(float(profit))

        if category == "Meat":
            #  print(region, category, profit)
            meat_profit_list.append(float(profit))

        if category == "Beverages":
            #  print(region, category, profit)
            beverages_profit_list.append(float(profit))

        if category == "Office Supplies":
            #  print(region, category, profit)
            office_supplies_profit_list.append(float(profit))

        if category == "Cosmetics":
            #  print(region, category, profit)
            cosmetics_profit_list.append(float(profit))

        if category == "Snacks":
            #  print(region, category, profit)
            snacks_profit_list.append(float(profit))

        if category == "Personal Care":
            #  print(region, category, profit)
            personal_care_profit_list.append(float(profit))

        if category == "Household":
            #  print(region, category, profit)
            household_profit_list.append(float(profit))

        if category == "Baby Food":
            #  print(region, category, profit)
            baby_food_profit_list.append(float(profit))

        if category == "Vegetables":
            #  print(region, category, profit)
            vegetables_profit_list.append(float(profit))

        if category == "Cereal":
            #  print(region, category, profit)
            cereal_profit_list.append(float(profit))

        if region == "Sub-Saharan Africa":
            sub_saharan_africa_profit_list.append(float(profit))

        if region == "Middle East and North Africa":
            mideast_and_north_africa_profit_list.append(float(profit))

        if region == "Australia and Oceania":
            oceania_profit_list.append(float(profit))

        if region == "Europe":
            europe_profit_list.append(float(profit))

        if region == "Asia":
            asia_profit_list.append(float(profit))

        if region == "Central America and the Caribbean":
            c_america_and_caribbean_profit_list.append(float(profit))

        if region == "North America":
            n_america_profit_list.append(float(profit))

fruits_sum = sum(fruits_profit_list)
clothes_sum = sum(clothes_profit_list)
meat_sum = sum(meat_profit_list)
beverages_sum = sum(beverages_profit_list)
office_supplies_sum = sum(office_supplies_profit_list)
cosmetics_sum = sum(cosmetics_profit_list)
snacks_sum = sum(snacks_profit_list)
personal_care_sum = sum(personal_care_profit_list)
household_sum = sum(household_profit_list)
baby_food_sum = sum(baby_food_profit_list)
vegetables_sum = sum(vegetables_profit_list)
cereal_sum = sum(cereal_profit_list)

sub_saharan_africa_sum = sum(sub_saharan_africa_profit_list)
mideast_and_north_africa_sum = sum(mideast_and_north_africa_profit_list)
oceania_sum = sum(oceania_profit_list)
europe_sum = sum(europe_profit_list)
asia_sum = sum(asia_profit_list)
c_america_and_caribbean_sum = sum(c_america_and_caribbean_profit_list)
n_america_sum = sum(n_america_profit_list)

print("The total profit for the Fruits category is %f" % fruits_sum)
print("The total profit for the Clothes category is %f" % clothes_sum)
print("The total profit for the Meat category is %f" % meat_sum)
print("The total profit for the Beverages category is %f" % beverages_sum)
print("The total profit for the Office Supplies category is %f" % office_supplies_sum)
print("The total profit for the Cosmetics category is %f" % cosmetics_sum)
print("The total profit for the Snacks category is %f" % snacks_sum)
print("The total profit for the Personal Care category is %f" % personal_care_sum)
print("The total profit for the Household category is %f" % household_sum)
print("The total profit for the Baby Food category is %f" % baby_food_sum)
print("The total profit for the Vegetables category is %f" % vegetables_sum)
print("The total profit for the Cereal category is %f" % cereal_sum)
print()
print("The total profit for the Sub-Saharan Africa region is %f" % sub_saharan_africa_sum)
print("The total profit for the Middle East and North Africa region is %f" % mideast_and_north_africa_sum)
print("The total profit for the Australia and Oceania region is %f" % oceania_sum)
print("The total profit for the Europe region is %f" % europe_sum)
print("The total profit for the Asia region is %f" % asia_sum)
print("The total profit for the Central America and the Caribbean region is %f" % c_america_and_caribbean_sum)
print("The total profit for the North America region is %f" % n_america_sum)
print()

list_of_c_sums = [fruits_sum, clothes_sum, meat_sum, beverages_sum, office_supplies_sum, cosmetics_sum,
                  snacks_sum, personal_care_sum, household_sum, baby_food_sum, vegetables_sum, cereal_sum]
list_of_c_types = ["Fruits", "Clothes", "Meat", "Beverages", "Office Supplies", "Cosmetics",
                   "Snacks", "Personal Care", "Household", "Baby Food", "Vegetables", "Cereal"]
index = list_of_c_sums.index(max(list_of_c_sums))
print("The top category is %s." % list_of_c_types[index])

list_of_r_sums = [sub_saharan_africa_sum, mideast_and_north_africa_sum, oceania_sum,
                  europe_sum, asia_sum, c_america_and_caribbean_sum, n_america_sum]
list_of_r_types = ["Sub-Saharan Africa", "Middle East and North Africa", "Australia and Oceania",
                   "Europe", "Asia", "Central America and the Caribbean", "North America"]
index = list_of_r_sums.index(max(list_of_r_sums))
print("The top region is %s." % list_of_r_types[index])
