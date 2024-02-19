class myBird:
    
    def __init__(self):
        print("myBird Class constructor is executing .....")

    def whatType(self):
        print("I am a bird ")

    def canSwim(self):
        print("i can swaim ")

class myPegwin(myBird):

    def __init__(self):
        super().__init__()
        print("myPegwin class is executing ")

    def whoisthis(self):
        print("I am a pegwig")

    def canRun(self):
        print("I can run faster ")

'''myPegwin is a subclass of myBird . myPegwin will inherit aall the attributes and methods of myBirds '''
