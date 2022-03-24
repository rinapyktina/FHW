if __name__ == "__main__":
    path = input("Enter a path to file: ")
    with open(path, "r", encoding="utf-8") as f:
        a = [int(i) for i in f]

    even_count = 0
    evens = 0
    for i in a:
        if i % 2 == 0:
            even_count += 1
            evens += i

    average = evens / even_count

    count = 0
    max_sum = 0
    for i in range(len(a)):
        if i != len(a) - 1:
            if (a[i] % 3 == 0 or a[i + 1] % 3 == 0) and (a[i] < average or a[i + 1] < average):
                count += 1
                max_sum = max(max_sum, a[i] + a[i + 1])

    print(count, max_sum)