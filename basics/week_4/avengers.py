def adding(lista = []):
    new_member = input("Enter new hero: ")
    lista.append(new_member)

def removing(lista = []):
    rejected = input("Enter hero to be removed: ")
    if rejected in lista:
        lista.remove(rejected)

def printing(lista = []):
    for hero in lista:
        print(f"The might {hero} is part of Avengers!")

def run():
    avengers = []
    while True:
        opt = int(input("Avengers, Assemble!\n\n1-Add a menber\n2-Remove a menber\n3- Check on team\n4-Exit\nOption:"))
        if opt == 1:
            adding(avengers)
        elif opt == 2:
            removing(avengers)
        elif opt == 3:
            printing(avengers)
        elif opt== 4:
            break
        else:
            print("Sort yourself out!")

run()




