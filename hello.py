def main():
    name = input("what your name ?")
    print(hello(name))
    

def hello(to="world"):
    return f"hello, {to}"


def test_hello():
   assert hello("David") == "hello, David"
   assert hello("Min")   == "hello, Phyo"

if __name__ == "__main__":
    main()