class Head:
    def __init__(self):
        self.eyes = 2
        self.nose = 1
        self.mouth = 1


class Hand:
    def __init__(self):
        self.fingers = 5


class Arm:
    def __init__(self,side,hand):
        self.side = side
        self.hand = hand


class Feet:
    def __init__(self):
        self.toes = 5


class Leg:
    def __init__(self,side,feet):
        self.side = side
        self.feet = feet


class Torso:    
    def __init__(self,head,right_arm,left_arm,right_leg,left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg


class Human:
    def __init__(self, name, torso):
        self.name = name
        self.torso = torso


    def describe(self):
        print(f"Human: {self.name}")
        print(f"Head -> Eyes: {self.torso.head.eyes}, Nose: {self.torso.head.nose}, Mouth: {self.torso.head.mouth}")
        print(f"Arms -> Left hand fingers: {self.torso.left_arm.hand.fingers}, Right hand fingers: {self.torso.right_arm.hand.fingers}")
        print(f"Legs -> Left foot toes: {self.torso.left_leg.feet.toes}, Right foot toes: {self.torso.right_leg.feet.toes}")


head = Head()
left_hand = Hand()
right_hand = Hand()
left_arm = Arm("left", left_hand)
right_arm = Arm("right", right_hand)
left_feet = Feet()
right_feet = Feet()
left_leg = Leg("left", left_feet)
right_leg = Leg("right", right_feet)
torso = Torso(head, right_arm, left_arm, right_leg, left_leg)

person = Human("Abner",torso)
person.describe()