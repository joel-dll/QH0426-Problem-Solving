def interests():
    print("Enter all your interests, one after another or \"Stop\" to stop")
    s1 = set()
    interest = ""
    while True:
        interest = input()
        if interest.lower() == "stop":
            break
        s1.add(interest)
    return s1

def tinderDaSecond():
    print("First person: ")
    p1 = interests()
    print("Second person: ")
    p2 = interests()
    common = p1.intersection(p2)
    if len(common) >= 3:
        print(f"You are a made in havean! You have {len(common)} in common")
    else:
        print("Oh no. It's not gonna work. FInd another person")

tinderDaSecond()