class person:
    distance = 15
    def walking(self, distance):
        location = "Goa"
        self.distance = distance
        print(self.distance)

    def running(self):
        print(self.distance)


ayush = person()
ayush.walking(30)
ayush.running()
