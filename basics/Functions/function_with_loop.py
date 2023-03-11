def cross_bridge(steps):

    for i in range(steps):
        print("Crossed step.")
    if steps <= 5:
        print("We must keep going!")
    else:
        print("The bridge is collapsing!")


cross_bridge(3)
cross_bridge(6)


