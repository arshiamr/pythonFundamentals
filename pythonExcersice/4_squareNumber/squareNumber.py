#4. Write a program that takes a number and calculates its square
def main():
    num=int(input("Enter Your Number : "))
    return squareNumber(num)
def squareNumber(number):
    return f"The square of your number is : {number*number}" 

if __name__ == "__main__":
    print(main())