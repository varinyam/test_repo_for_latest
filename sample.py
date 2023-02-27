def printRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12

    while number:
        div = number // num[i]
        number %= num[i]

        while div:
            print(sym[i], end = "")
            div -= 1
        i -= 1

# Driver code
if __name__ == "__main__":
    number = 6
    print("Roman value is:", end = " ")
    printRoman(number)

x,y,z=-1,1,0
for i in range(0,10):
    z=x+y
    x=y
    y=z
    print(z)
