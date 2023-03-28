import os
# MOVING FROM ONE FOLDER TO ANOTHER
path = os.getcwd()
print(f"My path is {path}")


#path=os.getcwd()
#print(path)
#os.chdir('../demos/')


with open("data_.txt", 'r') as file:  #r(read) is a method
    for data in file:
        data = data.rstrip("\n")
        fname, lname, depart, loc=data.split(', ')
        print("Firstname: ", fname)
        print("Lastname: ", lname)
        print("Department: ", depart)
        print("Location: ", loc)