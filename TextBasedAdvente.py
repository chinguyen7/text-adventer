class Point():
    def __init__(self, x_val, y_val):
        self.x_coord = x_val
        self.y_coord = y_val
    
    def move(self, dx, dy):
        self.x_coord += dx
        self.y_coord += dy
    
    def __str__(self):
        return "( " + str(self.x_coord) + ", " + str(self.y_coord) + " )"
        
    def multi(self, mn):
        self.x_coord *= mn
        self.y_coord *= mn
        
p1 = Point(0,0)
print(p1)
p1.move(1,1)
print(p1)
p1.multi(3)
print(p1)

class Des():
    def __init__(self, question, answer):
        self.question = question
        self.answer_list = answer
        self.connections = []
        
    def make_choice(self):
        print (self.question)
        choice = input(str(self.answer_list))
        while choice not in self.answer_list:
            print("Invalid Answer")
            choice = input(str(self.answer_list))
        return choice
    
    def connectAndPick(self, con1, con2):
        choice = self.make_choice()
        self.connections.append(con1)
        self.connections.append(con2)
        if choice == self.answer_list[0]:
            self.connection = self.connections[0]
        if choice == self.answer_list[1]:
            self.connection = self.connections[1]
        
        return str(self.connection)
        

start = Des("Left or right?", ["left", "right"])
left = Des("You find a mason. Claim the manson?", ["yes", "no"])
right = Des("You find a fire place. Go inside the fire?", ["go in", "stay out"])
fireplace = Des("You see a fairy, follow her?", ["follow", "don't follow"])
follow = Des("You find a fairy viilage. Do you party with them?", ['party', 'don\'t party'])
claim = Des("You claim the manson. Do the paperwork?", ['yes','no'])
inside = Des("You don\'t claim the mason. Go inside the manson?", ['yes','no'])


start.connectAndPick(left, right)
left.connectAndPick(claim, inside)  
right.connectAndPick(fireplace, "You freez to death due to the cold.")
fireplace.connectAndPick(follow, "Get killed by angry fairies.")
follow.connectAndPick("You live forever with the fairies", "You get killed out into the cold and die.")
inside.connectAndPick("Steal stuff.", "Stay inside and wait.")
claim.connectAndPick("You do the paperwork and get a free mason.", "You don/'t do the paperwork and get sued and jailed by the real owner.")

        