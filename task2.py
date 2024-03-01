# Write a program that reads in a whole number and divides it by 3 and displays the result with three decimal places if they exist (rounded up). For example, if the user enters 2 the program should display 0.667. For example, if the user enters 9999 the program should display 3,333.0. The file should be named task2.py.

# Menggunakan Library math untuk perhitungan
import math

def main():
    # Inputan Angka dari user
    num = int(input("Masukan Angka: "))

    # Total Inputan di bagi 3
    result = num / 3

    # Hasil pembagian di format menjadi
    formatted_result = "{:.3f}".format(result)
    print("Result:", formatted_result)

if __name__ == "__main__":
    main()
