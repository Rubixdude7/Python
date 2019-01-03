class Noun:
    sing = ("os","om","osyo","oey","ead")
    plr  = ("oes","ons","oHom","omos","omos")

    def __init__(self, word):
        self.root = word

    def decline(self):
        for i in range(5):
            print (self.root + self.sing[i] + "\t"  + self.root + self.plr[i])


text = Noun("nisd")
text.decline()
