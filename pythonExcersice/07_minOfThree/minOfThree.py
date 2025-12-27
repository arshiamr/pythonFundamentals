#7. Write a program that finds the smallest number among three numbers
def main():
    numbers=[]
    for i in range(3):
        num=int(input(f"Enter Your {i} Number : "))
        numbers.append(num)
    return minNumber(numbers)
def minNumber(numbers):
    return f"{min(numbers)} is the minimum number"
   
if __name__ == "__main__":
    print(main())