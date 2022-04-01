def fibo(count):
    a, b = 0, 1
    for i in range(count):
        print(a)
        a, b = b, a+b


def main():
    fibo(count=10)


if __name__ == "__main__":
    main()
