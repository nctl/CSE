import csv


def validate(num: str):
    all_digits = list(num)
    if len(num) is not 16:  # The INITAL list i.e. before removing the last digit
        return False
    last_digit = all_digits[15]
    all_digits.pop(15)
    all_digits = reverse_it(all_digits)
    multiply_odd_digits(all_digits)
    total_sum = sum(all_digits)
    return mod_10(total_sum, last_digit)


def reverse_it(all_digits: list):
    all_digits = all_digits[::-1]
    return all_digits


def multiply_odd_digits(num: list):
    for index in range(len(num)):
        num[index] = int(num[index])
        if index % 2 == 0:
            num[index] *= 2
            if num[index] > 9:
                num[index] -= 9


def mod_10(total_sum, last_digit):
    if int(total_sum) % 10 == int(last_digit):
        return True
    else:
        return False


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Writing File...")
        for row in reader:
            num = row[0]
            if validate(num):
                writer.writerow(row)
        print("Done")
