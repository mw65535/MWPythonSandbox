import calculator


def main():
    a, b = 10, 3
    print(f"{a} + {b} = {calculator.add(a, b)}")
    print(f"{a} - {b} = {calculator.subtract(a, b)}")
    print(f"{a} * {b} = {calculator.multiply(a, b)}")
    print(f"{a} / {b} = {calculator.divide(a, b)}")


if __name__ == "__main__":
    main()
