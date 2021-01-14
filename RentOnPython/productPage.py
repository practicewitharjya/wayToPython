class Product:
    productList = ["Fridge", "TV", "Bed","Chair", "Table", "Filter"]

    def displayProduct(self):
        print("We have all the following Products: \n")
        print("###############")
        for item in self.productList:
            print(item)
        print("###############")

    def rentAProduct(self, item):
        self.productList.remove(item)
        print(f"You have successfully Rented: {item}")

    def returnProduct(self, item):
        self.productList.append(item)
        print(f"{item} has been returned to RentByPython")