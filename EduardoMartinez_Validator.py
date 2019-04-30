import csv

# with open("Book1.csv", 'r') as old_csv:
#     with open("CreditCardNumlist.csv", 'w', newline='') as new_csv:
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         print("Writing File...")
#
#         for row in reader:
#             old_number = row[0]
#             if validate(old_number):
#                 writer.writerow(row)
#         print("Done")


def validate(num: str):
    all_digits = list(num)
    last_digit = all_digits[15]
    all_digits.pop(15)
    all_digits = reverse_it(all_digits)
    print(all_digits)


def reverse_it(all_digits: list):
    all_digits = all_digits[::-1]
    return all_digits


def multiply_odd_digits(num: str):
    for index in range(len(num)):
        integer_version = int(num[index])


def subtract_large_numbers(num: str):
    for i in all_digits:
        if i > 9:
            i -= 9
