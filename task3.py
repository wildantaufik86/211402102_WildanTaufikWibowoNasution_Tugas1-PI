# Write a program that reads in a number and prints either Small, Medium or Large depending on if the number is below 100 or above 200. For example, if the user enters 150 the program should display “Medium”. Another example is if the user enters 50 the program should display “Small”. The file should be named task3.py.

def main():
    # Inputan Angka
    number = float(input("Masukan Angkaa: "))

    # Fungsi untuk cek angka
    if number < 100:
        print("Small")
    elif number > 200:
        print("Large")
    else:
        print("Medium")

if __name__ == "__main__":
    main()
