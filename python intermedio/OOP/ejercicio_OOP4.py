class Head:
    def __init__(self):
        self.eyes = 2
        self.nose = 1
        self.mouth = 1


class Torso:    
    def __init__(self):
        self.head = 1
        self.arms = 2
        self.belly = 1


class Arm:
    def __init__(self,side):
        self.side = side
        self.hand = Hand()


class Hand:
    def __init__(self):
        self.fingers = 5


class Leg:
    def __init__(self,side):
        self.side = side
        self.feet = Feet()


class Feet:
    def __init__(self):
        self.toes = 5


class Human:
    def __init__(self, name):
        self.name = name
        self.head = Head()
        self.torso = Torso()
        self.left_arm = Arm("left")
        self.right_arm = Arm("right")
        self.left_leg = Leg("left")
        self.right_leg = Leg("right")


    def describe(self):
        print(f"Human: {self.name}")
        print(f"Head -> Eyes: {self.head.eyes}, Nose: {self.head.nose}, Mouth: {self.head.mouth}")
        print(f"Torso -> Head: {self.torso.head}, Arms: {self.torso.arms}, Belly: {self.torso.belly}")
        print(f"Arms -> Left hand fingers: {self.left_arm.hand.fingers}, Right hand fingers: {self.right_arm.hand.fingers}")
        print(f"Legs -> Left foot toes: {self.left_leg.feet.toes}, Right foot toes: {self.right_leg.feet.toes}")


person = Human("Abner")
person.describe()