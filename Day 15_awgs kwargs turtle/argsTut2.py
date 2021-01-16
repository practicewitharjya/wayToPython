# def sum(num1, num2, num3):
#     print("sum = ", num1+num2+num3)
#
#
# sum(2,3,6,8)

def add(*agrs):
    sum = 0
    for n in agrs:
        sum = sum +n

    print("Sum: ", sum)

add(2, 3, 5, 6, 10,35, 377, 4,6,7,9,5,4,135,3,6,6,7,8,9)
