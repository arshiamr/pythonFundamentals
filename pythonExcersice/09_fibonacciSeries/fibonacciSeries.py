#9. Write a program that generates the first n Fibonacci numbers
def main():
    num=int(input("Enter Your Number : "))
    return fib(num)
def fib(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fib(number-1)+fib(number-2)

if __name__ == "__main__":
    print(main())