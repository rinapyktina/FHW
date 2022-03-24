if __name__ == "__main__":
    path = input("Enter a path to file: ")
    with open(path, "r", encoding="utf-8") as f:
        a = [int(i) for i in f]

    count = 0
    max_sum = 0
    for i in range(len(a)):
        if i != len(a) - 1:
            if (a[i] % 5 == 0 or a[i + 1] % 5 == 0) and ((a[i] + a[i + 1]) % 7 == 0):
                count += 1
                max_sum = max(max_sum, a[i] + a[i + 1])

    print(count, max_sum)