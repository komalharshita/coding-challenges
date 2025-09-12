class Sports:
    outdoor = True

    def __init__(self, sports_name, sports_team):
        self.sports_name = sports_name
        self.sports_team = sports_team

    def print_info(self):
        print(f"{self.sports_name} - {self.sports_team}")