import csv

# # with open("Book1.csv", 'r') as old_csv:
# #     reader = csv.reader(old_csv)
# #     for row in reader:
# #         old_number = row[0]
# #         print(old_number)
# #         print(int(old_number) + 1)
#
# with open("Book1.csv", 'r') as old_csv:
#     with open("MyNewFile.csv", 'w', newline='') as new_csv:
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         print("Processing...")
#
#         for row in reader:
#             old_number = row[0]
#             first_number = int(old_number[0])
#             if first_number % 3 == 0:
#                 writer.writerow(row)
#         print("Done")
#         print("Check file (MyNewFile).")


def first_num_odd(num: str):
    first_num = int(num[0])
    if first_num % 2 == 1:  # odd numbers only
        return True
    return False


def second_num_even(num: str):
    second_num = int(num[1])
    if second_num % 2 == 0:  # even numbers only
        return True
    return False


def validate(num: str):
    if first_num_odd(num) and second_num_even(num):
        return True
    return False


def reverse(string):
    string = string[::-1]
    return string


print(reverse("dlroW olleH"))


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Writing File...")

        for row in reader:
            old_number = row[0]
            if validate(old_number):
                writer.writerow(row)
        print("Done")
        print("Check file (MyNewFile).")
