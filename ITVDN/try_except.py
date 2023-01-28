'''
a = 12
b = 0
try:
    c = a/b
except:
    c = 0
    print("Division on zero")
print(c)
'''
'''
try:
    print(int("abc"))
except ValueError as error:
    print(error)
'''
'''
print ('Calculator')

try:
    a = float(input("a: "))
    b = float(input("b: "))

    print(a/b)
except (ZeroDivisionError, ValueError) as error:
    print(error)

print("done!")
print()
'''
'''
def main():
    while True:
        try:
            first_num = float(input("num_1: "))
            second_num = float(input("num_2: "))
            print("Result:", first_num / second_num)
            break
        except(ValueError, ZeroDivisionError) as error:
            print("Error! >", error)
            print("one more try...")

if __name__ == "__main__":
    main()
'''
import warnings

name = input("What's your name and sur?: ")

if name.count(" ") != 1:
    warnings.warn("Are you arabian?")

print("Hello", name, "!", sep=" ")