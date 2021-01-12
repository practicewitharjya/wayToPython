def add(a, b):
    if (type(a) is int and type(b) is int):
        return a+b
    else:
        raise TypeError('You have to enter integer value only')

print(add("Python", "YGFCG"))