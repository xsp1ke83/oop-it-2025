def main():
    print("Програма для перевірки чисел")
    num = int(input("\nВведіть ціле число: "))

    if num > 0:
        print("\nЧисло додатнє")
    elif num < 0:
        print("\nЧисло від’ємне")
    else:
        print("\nЧисло дорівнює нулю")

    print("\nВивід чисел від 1 до", num)
    for i in range(1, num + 1):
        print(i, end=" ")

    print("\n")

    print("Зворотний відлік:")
    while num > 0:
        print(num, end=" ")
        num -= 1

if __name__ == "__main__":
    main()
