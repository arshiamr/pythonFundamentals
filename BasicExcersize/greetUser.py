#2. Write a program that takes the user's name and greets them
def main():
    userName=input("What's Your Name? :")
    return (sayHello(userName))
def sayHello(Name):
    return f"Hello, {Name}"

if __name__ == "__main__":
    print(main())