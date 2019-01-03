class GothicNoun:
    def __init__(self, word):
        self.root = word
    def nominative(self):
        return self.root + "s"
    def accusative(self):
        return self.root
    def genitive(self):
        return self.root + "is"
    def dative(self):
        return self.root + "a"

myWord = GothicNoun("dag")
print(myWord.nominative())
print(myWord.accusative())
input()
