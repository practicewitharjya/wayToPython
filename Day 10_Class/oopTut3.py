"""
You are my friend
What is your skil Pradip?
Pradip, what is your skil?
"""

class IPhoneMobile:
    screen_size = 6     # Class variable
    camera = '20 MP'    # Class variable

    # Instance Method
    def calling(self):
        print("This mobile has calling feature")

    # Instance Method
    def videoCalling(self, apps):
        self.apps = apps
        return "You are using a good mobile"

    # Instance Method
    def navigation(self, apps, loc):
        #Instance variable
        self.apps = apps
        self.loc = loc
        print(f"You have choosen {self.apps} to reach {self.loc}")



iphone13 = IPhoneMobile()
#print(iphone13.screen_size)
#iphone13.calling()
# IPhoneMobile.videoCalling(iphone13,"Whatsapp")
print(iphone13.videoCalling("Whatsapp"))
#iphone13.navigation("Map", "Bangalore")



