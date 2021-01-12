"""
Encapsulation: It describes the idea of wrapping data and method that should work as a single unit
This put restrictions on accessing variables and method directly to prevent the data change
"""
class Indian:
    __money = 100000  # Private variable

    def __pmfundcare(self, rupee):  # Private method
        self.__money = self.__money + rupee
        return self.__money


ayush = Indian()
shyam = Indian()
# Below are not allowed
ayush.__money
ayush.__pmfundcare(1000)