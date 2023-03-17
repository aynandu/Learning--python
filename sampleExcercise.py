import random
def find_random_num(guess,answer):
    if 0 < guess < 6:
        if guess==answer:
            print("You are a genious")
            return True
    else:
        print("enter a  value between 1 to 5")
    

if __name__ =='__main__':
    answer = random.randint(1,5)
    print(type(answer))
    while True:
        try:
            guess = int(input('Guess a Number: ')) 
            if (find_random_num(guess,answer)):
                break   
        except ValueError:
                print("please enter a number")
                continue

  