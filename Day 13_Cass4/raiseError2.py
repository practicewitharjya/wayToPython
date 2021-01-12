def div(a, b):
    if b!=0:
        return a/b
    else:
        raise ZeroDivisionError("Please don't enter 0 as 2nd number")


div(3, 0)