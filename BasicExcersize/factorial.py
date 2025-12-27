#8. Write a program that takes a number and calculates its factorial
def main():
    num=int(input("Enter Your Number : "))
    return factNumber(num)
def factNumber(number):
    fact=1
    for i in range(number,0,-1):
        fact*=i
        
    return f"The factorial of your number is : {fact}" 

if __name__ == "__main__":
    print(main())