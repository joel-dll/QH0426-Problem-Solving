import matplotlib.pyplot as plt


def coffee_sleep(n=5):
    coffee = []
    sleep = []
    for i in range(n):
        coffee.append(int(input("Enter amount of coffee you drink per week: ")))
        sleep.append(int(input("Enter average sleep duration per night: ")))
    return coffee, sleep

def movies(n=5):
    movie = {}
    for i in range(n):
        genre = input("Enter your favourite movie genre: ")
        movie[genre] = movie.get(genre, 0) + 1
    return movie

def music(n=5):
    songs={}
    for i in range(n):
        genre = input("Enter your favourite music genre: ")
        songs[genre] = songs.get(genre, 0) + 1
    return songs

def mm_vs_dd(n=5):
    mm,dd = 0,0
    for i in range(n):
        ans = input("Who wins? Micky Mouse or Donald Duck?")
        if ans.lower() == 'mm':
            mm += 1
        elif ans.lower() == "dd":
            dd += 1
        else:
            print("That is not a valid answer.")
    return [mm,dd]

def run():
    fig = plt.figure()
    ax1 = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,3)
    ax4 = fig.add_subplot(2,2,4)

    n = int(input("Enter number of respondents: "))
    c_s = coffee_sleep(n)
    ms = movies(n)
    ss = music(n)

    ax1.plot(c_s[0],c_s[1],"rx")
    ax1.set_xlabel("Coffee intake(cups per day)")
    ax1.set_ylabel("Sleep in h per night")
    ax1.set_title("Coffee vs Sleep")

    ax2.pie(ms.values(), labels=ms.keys(),autopct = "%1.1f%%")
    ax2.set_title("Movie Preferences")

    ax3.pie(ss.values(), labels=ss.keys(), autopct = "%.f%%")
    ax3.set_title("Music Preferences")

    ax4.bar(["MM","DD"], mm_vs_dd(n))
    ax4.set_xlabel("Characters")
    ax4.set_ylabel("Frequency")
    ax4.set_title("Big battle of 2 best characters!")

    plt.tight_layout()
    plt.show()

run()