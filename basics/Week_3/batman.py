from random import randint

def batman_punch(strength = 5,technique = 8 ):
    punch_power = strength * 0.4 + technique * 0.6
    return punch_power
def fight_scene(number = 2,enemy_strength = 3, ):
    total_strength = number * enemy_strength
    #bat_strength = batman_punch(int(input("Enter batman strength: ")),(int(input("Enter batman technique: "))))
    bat_strength = batman_punch(randint(0,10), randint(0,10))
    if bat_strength >= total_strength:
        return "Batman Wins!"
    else:
        return "Batman Looses"
def roberry_escape(number_of_cars):
    if number_of_cars > 5:
        return "Batman is caught"
    else:
        return "Batman escapes"

def run():
    scene = fight_scene()
    #escape = roberry_escape(3)
    escape = roberry_escape(randint (2,12))
    print(f"After a long fight,{scene}.Afterwards, police chase him and {escape}.")


run()



