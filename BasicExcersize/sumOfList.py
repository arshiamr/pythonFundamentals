#10. Write a program that creates a list of numbers and calculates their sum
import random
def main():
    num1=int(input("Enter Your size of list: "))
    num2=int(input("Enter Your low Number : "))
    num3=int(input("Enter Your high Number : "))
    yourList=generate_random_list(num1,num2,num3)
    return( yourList ,f"sum of this list is {sumList(yourList)}")
def generate_random_list(size, low, high):
    return [random.randint(low, high) for _ in range(size)]
def sumList(myList):
    total = 0
    for n in myList:
        total += n
    return total
if __name__ == "__main__":
    print(main())