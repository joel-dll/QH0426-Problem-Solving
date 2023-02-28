battery_found = False
while (battery_found == False):

    print("Where should I look?")
    ans1 = input()

    if ans1 == "in the bedroom":
        print("Where in the bedroom should I Look?")
        ans2 = input()
        if ans2 == "under the bed":
            print("found some shoes but no battery")
        else:
            print("Found some mess but no battery")
    elif ans1 == "in the bathroom":
        print("where in the bathroom shoud I look?")
        ans2 = input()
        if ans2 == "in the bathub":
            print("Found rubber duck but no battery")
        else:
            print("Found wet surface but no battery")
    elif ans1 == "in the lab":
        print(" where in the lab should look ?")
        ans2 = input()
        if ans2 == "on the table":
            print("yes! I found the battery")
            battery_found = True
        else:
            print("Found some tools but no battery")
    else:
        print("do not know where that is but i will keep looking")