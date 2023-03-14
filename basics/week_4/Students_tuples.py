def generate():
    name = input("Enter name of a student: ")
    mkr = float(input(f"Enter mark for {name}:"))
    return name,mkr

def list_of_stds(n):
    stud_list = []
    for i in range(n):
        stud_list.append(generate())
    return stud_list

def average(lista = []):
    total = 0
    for tup in lista:
        total += tup[1]
    if len(lista) > 0:
        avg = total/len(lista)
    else:
        avg = 0
    return avg

def run():

    stud_list = list()
    while True:
        opt = int(input("Menu:\n1-Populate list of students\n2-Calculate avareage\n3- Calculate average mark\n3-Change mark for student\n4-Exit\n"))

        if opt == 4:
            break
        elif opt == 1:
            n = int(input("Enter number of students: "))
            stud_list.extend(list_of_stds(n))
        elif opt == 2:
            print(f"The average mark is {average(stud_list):.2f}")
        elif opt == 3:
            name = input("Who mark to update:")
            for student in stud_list:
                if student[0].upper == name.upper():
                    n_mark = float(input(f"Enter new mark for {name}: "))
                    stud_list.remove(student)
                    stud_list.append((name, n_mark))
        else:
            print("Somenthing is wrong. You fool!")
run()