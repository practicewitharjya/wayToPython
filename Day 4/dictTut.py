dict1 = {"Math": 100, "Chem": 98}
# Dict is a key: value pair
# print(type(dict1))

loginDict = {
                'userId': "arjya@gmail.com",
                'password': 'Test1234'
            }
# print("My password is", loginDict['password'])
loginDict['url'] = 'www.google.com'
#print(loginDict)

loginDict.pop('password')
#loginDict.clear()

print(loginDict)