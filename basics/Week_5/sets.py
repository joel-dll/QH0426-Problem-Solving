#Initialise empty set
s = set()
#Initialise non-empty set
colours = {"blue", "red", "yellow", "purple", "red"}
print(colours)
#Adding elements into a set
colours.add("green")
colours.add("navy blue")
print(colours)
colours = colours.union({"black", "magenta", "crimson", "brown", "purple"})
print(colours)
#Remove item from a set
if "yellow" in colours:
    colours.remove("yellow")
print(colours)
#Sets are heterogeneous and duplicates are not allowed
colours.add(99)
colours.add(True)
print(colours)
#Check membership
if "yellow" in colours:
    print("Yay - I like yellow!")
else:
    print("Sad days, no yeallow :(")


c = {"brown", "turquise", "cyan", "coquelicot", "pink", "red"}

#Union = join 2 sets togehter, not keeping dupicates (each element appears 1 time)
c2 = colours.union(c)
print(f"c is {c}")
print(f"c2 is {c2}")
print(f"colours is {colours}")

#Intersection - looking at common values of 2 collections
c3 = c.intersection(colours)
print(f"c3 is {c3}")

#Difference - keep elements of one set that are NOT part of the other
c4 = colours.difference(c)
c5 = c.difference(colours)
print(f"c4 is {c4}")
print(f"c5 is {c5}")