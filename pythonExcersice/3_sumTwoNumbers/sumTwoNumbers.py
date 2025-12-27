#3. Write a program that takes two numbers and displays their sum
def main():
    num1=int(input("Enter Your First Number : "))
    num2=int(input("Enter Your Second Number : "))
    return sumTwoNumber(num1,num2)
def sumTwoNumber(number1,number2):
    return f"The sum of your numbers is : {number1+number2}"


if __name__ == "__main__":
    print(main())