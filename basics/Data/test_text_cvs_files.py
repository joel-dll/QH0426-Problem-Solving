import os
# MOVING FROM ONE FOLDER TO ANOTHER
path = os.getcwd()
print(f"\n\nMy path is {path}")
path = os.chdir('./staff/')



#path=os.getcwd()
#print(path)
#os.chdir('../demos/')


with open("data.txt", 'r') as file:
    for data in file:
        data = data.rstrip("\n")
        fname, lname, depart, loc=data.split(', ')
        print("\n...................\n")
        print("Firstname: ", fname)
        print("Lastname: ", lname)
        print("Department: ", depart)
        print("Location: ", loc)
