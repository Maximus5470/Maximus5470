def main():
    num = get_num()
    meow(num)

def get_num():
    while True:
        n = int(input("Enter n value: "))
        if n > 0:
            break
        else:
            print("Enter positive number")
            continue
    return n
def meow(n):
    for i in range(n):
        print("meow")


if __name__ == '__main__':
    main()
