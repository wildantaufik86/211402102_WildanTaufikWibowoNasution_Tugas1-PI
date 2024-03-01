# Write a program that reads in a number and prints either Small, Medium or Large depending on if the number is below 100 or above 200. For example, if the user enters 150 the program should display “Medium”. Another example is if the user enters 50 the program should display “Small”. The file should be named task3.py.

def main():
    # Inisialisasi sebuah variable untuk menampung total nilai
    total_sum = 0

    # Perulangan untuk membuat Inputan
    for i in range(5):
        number = int(input(f"Masukan Nilai {i+1}: "))
        total_sum += number

    # Output dari Total Inputan
    print("Total dari jumlah nilai adalah:", total_sum)

if __name__ == "__main__":
    main()
