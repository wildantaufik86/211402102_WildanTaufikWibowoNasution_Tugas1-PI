#Write a program that reads in numbers until a -1 is entered and prints the sum of all numbers entered. For example, if the user enters 5 10 15 -1 the program should display 30 (Each number will be separated by a carriage return). 30 is (5+10+15). The file should be named task5.py.

def main():
    # Inisialisasi variable total nilai
    total_sum = 0

    # Inputan angka
    # Fungsi
    while True:
        num = int(input("Masukan Nilai (-1 untuk berhenti): "))
        if num == -1:
            break  # Exit the loop if -1 is entered
        total_sum += num

    # Menampilkan seluruh total nilai yg terkumpul
    print("Total Nilai yg terkumpul adalah:", total_sum)

if __name__ == "__main__":
    main()
