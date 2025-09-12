class Sports:
 def __init__(self, sports_name, sports_type):
   self.name = sports_name 
   self.type= sports_type

golf = Sports("Golf", "Hand Sports")
print(golf.name)
print(golf.type)

class Car:
    def __init__(self, manufacturer, build_date):
        self.manufacturer = manufacturer
        self.build_date = build_date