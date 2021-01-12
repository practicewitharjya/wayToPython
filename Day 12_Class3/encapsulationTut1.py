class Indian:
    __money = 100000  # Private variable

    def __pmfundcare(self, rupee):  # Private method
        self.__money = self.__money + rupee
        return self.__money

    def donateInPmFund(self, money):
        return self.__pmfundcare(money)

ayush = Indian()
shyam = Indian()
# ayush.donateInPmFund(10000)
finalMoney = shyam.donateInPmFund(20000)
print("After donating by Shyam now the Money =",finalMoney)