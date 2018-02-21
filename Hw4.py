import random
class Game:
    def __init__(self,id):
        self.id =id
    def simulation(self):
        StartingValue =-250
        n_of_steps = 0
        j=0
        step=["H","T","H","T","H","T","H","T","H","T","H","T","H","T","H","T","H","T","H","T"]
        for j in range(0,len(step)):
           step[j]=random.choice(["H","T","H","T","H","T","H","T","T","T"])
           j=j+1
        for n_of_steps in range(0,18):
            if step[n_of_steps] == 'T' and step[n_of_steps+1]=='T' and step[n_of_steps+2]=='H':
                StartingValue +=100
                n_of_steps = n_of_steps + 3
            else:
                StartingValue +=0
                n_of_steps=+ 1
        return StartingValue

class Cohort:
    def __init__(self,id,pop_size):

        self.step=[]
        self.total_score=[]
        n=1
        while n<=pop_size:
            GameUnit=Game(id*pop_size+n)
            self.step.append(GameUnit)
            n+=1

    def SimulateCohort(self):
        for flip in self.step:
            value=flip.simulation()
            self.total_score.append(value)

    def get_expected_score(self):
        return sum(self.total_score)/len(self.total_score)

test = Cohort(1, 1000)
test.SimulateCohort()
print("The expected score is", test.get_expected_score())