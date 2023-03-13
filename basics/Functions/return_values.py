def sum_weights(beep_w, bop_w):
    sum_beep_bop = beep_w + bop_w
    return sum_beep_bop


def calc_avg_weight(beep_w, bop_w):
    result_avg = (beep_w + bop_w) / 2
    return result_avg


def run():

    print("What is the weight of Beep? ")
    beep_w = float(input())

    print("What is the weight of Bop?")
    bop_w = float(input())

    print("What would you like to calculate (sum or average)? ")
    action = input()

    if (action == "sum"):
        answer = sum_weights(beep_w, bop_w)
        print("The sum of Beep's and Bop's weight is {:.2f}".format(answer))
    elif (action == "average"):
        answer = calc_avg_weight(beep_w, bop_w)
        print("The average of Beep's and Bop's weight is {:.2f}".format(answer))
    else:
        print("I am not sure what you would like to do.")


run()
