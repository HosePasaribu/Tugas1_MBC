# Kalkulator Sederhana menggunakan Python
# Yesaya Pasaribu - Cyber Security

def add(num1, num2):
	return num1 + num2


def subtract(num1, num2):
	return num1 - num2


def multiply(num1, num2):
	return num1 * num2


def divide(num1, num2):
	return num1 / num2

print("Menu kalkulator sederhana Yesaya :\n" \
		"1. Penjumlahan\n" \
		"2. Pengurangan\n" \
		"3. Perkalian\n" \
		"4. Pembagian\n")



select = int(input("Silahkan pilih metode operasi 1, 2, 3, 4 :"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
	print(number_1, "+", number_2, "=",
					add(number_1, number_2))

elif select == 2:
	print(number_1, "-", number_2, "=",
					subtract(number_1, number_2))

elif select == 3:
	print(number_1, "*", number_2, "=",
					multiply(number_1, number_2))

elif select == 4:
	print(number_1, "/", number_2, "=",
					divide(number_1, number_2))
else:
	print("Invalid input")
