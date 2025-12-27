#6. Write a program that finds the largest number between two numbers
def main():
    num1=int(input("Enter Your First Number : "))
    num2=int(input("Enter Your Second Number : "))
    return largerTwoNumber(num1,num2)
def largerTwoNumber(number1,number2):
        if number1>number2 :
            return f"{number1} is larger"  
        else:
            return f"{number2} is larger"
   



if __name__ == "__main__":
    print(main())