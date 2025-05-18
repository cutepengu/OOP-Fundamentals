class Subject:
    def __init__(self, name, yrlvl, clscode, numstuen):
        self.name = name
        self.yrlvl = yrlvl
        self.clscode = clscode
        self.numstuen = numstuen

def display_info(self):
        return (f"Subject Name: {self.name}\n"
                f"Year Level: {self.yrlvl}\n"
                f"Class Code: {self.clscode}\n"
                f"Number of Students: {self.numstuen}")
