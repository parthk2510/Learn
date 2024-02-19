class myBird:
    def __init__(self):
        print("myBird class constructor is executing" )

    def whatType(self):
        print("I am a bird ")

    def canSwim(self):
        print("I can Swim ")


class myParrot:
    species="bird"

    def __init__(self , name , age):
        print("myParrot class constructor is execuitng ")
        self.name=name
        self.age=age
    
    def canSing(self,thiSong):
        return "{} can sing {} ..".format(self.name,thiSong)
    

class myPenguin(myBird):
    def whoisThis(self):
        print("I am pegwin ")

    def __init__(self, name, age):
        super().__init__()
        print("myPenguin class constructor is executing")
        self.name = name
        self.age = age


if __name__ == "__main__":
    penguin = myPenguin("Chilly", 5)
    penguin.whoisThis()
    penguin.whatType()
    penguin.canSwim()

    '''myBird is a base class ,myParrot is a seperate class , myPenguin is a sub-classof myBird'''