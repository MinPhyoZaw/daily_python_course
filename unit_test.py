def main():
    x = int(input("what is x? "))
    square(x)
    print(f"x is " ,square(x))

def square(n):
    return n + n

if "_name__" == "_main__":
    main()