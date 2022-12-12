print("----SCIENTIFIC CALCULATOR----")
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\n6.Square root\n7.Exponential\n8.Sine\n9.Cosine\n10.Tangent\n11.Radian to Degree\n12.Degree to Radian")
import math
ch="y"
while ch=="y":
    a = int(input("Choose your option: "))
    if a==1:
        print("      Addition      ")
        a1=float(input("Enter your First Number:"))
        b1=float(input("Enter your Second Number:"))
        print("Answer=",a1+b1)
    elif a==2:
        print("      Subtraction:      ")
        a1 = float(input("Enter your First Number:"))
        b1 = float(input("Enter your Second Number:"))
        print("Answer=", a1 - b1)
    elif a == 3:
        print("      Multplication      ")
        a1 = float(input("Enter your First Number:"))
        b1 = float(input("Enter your Second Number:"))
        print("Answer=", a1 * b1)
    elif a == 4:
        print("      Division      ")
        a1 = float(input("Enter your First Number:"))
        b1 = float(input("Enter your Second Number:"))
        print("Answer=", a1 / b1)
    elif a == 5:
        print("      Modulus      ")
        a1 = float(input("Enter your First Number:"))
        b1 = float(input("Enter your Second Number:"))
        print("Answer=", a1 % b1)
    elif a == 6:
        print("     Square root      ")
        a1 = int(input("Enter your Number:"))
        print("Answer=", a1 ** 0.5)
    elif a == 7:
        print("      Exponential      ")
        a1 = int(input("Enter your First Number:"))
        b1 = int(input("Enter your Second Number:"))
        print("Answer=",math.pow(a1,b1))

    elif a == 8:
        print("     Sine      ")
        a1 = float(input("Enter your Number:"))
        print("Answer=",math.sin(a1))

    elif a == 9:
        print("     Cosine      ")
        a1 = float(input("Enter your Number:"))
        print("Answer=",math.cos(a1))
    elif a == 10:
        print("     Tangent      ")
        a1 = float(input("Enter your Number:"))
        print("Answer=",math.tan(a1))
    elif a == 11:
        print("     Radian to Degree      ")
        a1 = float(input("Enter your Number:"))
        print("Answer=",math.degrees(a1))
    elif a == 12:
        print("     Degree to Radian      ")
        a1 = float(input("Enter your Number:"))
        print("Answer=",math.radians(a1))
    else:
        print("\tChoose a correct option")
    ch = input("Do you need to continue?(y/n): ")
    if ch=="n":
        print("\tThank You")
    elif ch=='y':
        pass
    else:
        print("\tEntered invalid input....Exiting")




