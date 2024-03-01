# Write a program using Python that reads in the user's salary and divides the number by 12 months. The monthly salary should be output to the console with 0 decimal places rounded up. For example, if the user enters 60000 the program should display 5000. The file should be named task1.py.

# Menggunakan Librart math untuk perhitungan Gaji
import math

def main():
    # Inputan Gaji
    salary = float(input("Masukan Gaji Anda: "))

    # Membagi ke 12 bulan total gaji yg di input
    monthly_salary = math.ceil(salary / 12)

    # Output nilai dari Hasil Pembagian
    print("Your monthly salary is:", monthly_salary)

if __name__ == "__main__":
    main()
