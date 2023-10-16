def main():
    x = get_Inp("Whats x? ")
    print(f"x is {x}")


def get_Inp(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


if __name__ == '__main__':
    main()
