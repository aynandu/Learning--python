class game():
    print ("Tom & Jerry")
    

class toss(game):
    def __init__(self,choose):
        self.choose=choose
    def toss_time(self):
        y = 'head' 
        n  = 'tail' 
        print('Choose y for Head , n for Tail')
        if self.choose== 'y':
            batting()  
        else:
            bowling()
    
class playerdetails(game):
    pass

class Computer_Player(game):
    pass

class batting(game):
    print('You are opt to bat')

class bowling(game):
     print('You are opt to bowl')


class scoreboard(game):
    pass

class fall_of_wickets(game):
    pass

class result():
    pass

toss_input = toss(input)
toss_input.toss_time()