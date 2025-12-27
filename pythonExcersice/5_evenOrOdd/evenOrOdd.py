#5. Write a program that determines whether a number is even or odd
def main():
    num=int(input("Enter Your Number : "))
    return evenOrOdd(num)
def evenOrOdd(number):
    if number % 2==0:
        return f"{number} is even"  
    else:
        return f"{number} is odd"
if __name__ == "__main__":
    print(main())