def display_ladder(steps):
    for i in range(steps):
        print(chr(124)+chr(32)+chr(124))
        print(chr(42)+chr(42)+chr(42))
    print(chr(124) + chr(32) + chr(124))
def create_ladder():
    print("How many steps remain? ")
    user_steps = int(input())
    display_ladder(user_steps)


create_ladder()