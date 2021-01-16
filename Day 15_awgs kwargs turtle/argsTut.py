# def mobile(brand, model, ram, camera):
#     print(f"{brand} {model} {ram} {camera}")
#
#
# mobile("Samsung", "S11", "3GB Ram", "64 MP", "256 GB", "6 inch")

def mobile(*details):
    print("I am inside function without any error")


mobile("Samsung", "S11", "3GB Ram", "64 MP", "256 GB", "6 inch")