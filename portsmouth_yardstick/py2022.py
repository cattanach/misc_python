from art import logo

yardstick = {
    "GP14":1130,
    "LASER":1100,
    "TOPPER":1365,
    "STREAKER":1128,
    "RS VISION":1137,
    "CONTENDER":969,
    "OPTIMIST":1642,
}

def portsmouth():

    def calculator(pn,seconds):
        return (seconds / pn) * 1000

    print(logo)

    boats = []
    times = []

    add_boat = True

    while add_boat:
        boat_class = input("\nWhat kind of boat? ").upper()
        race_time = float(input("How long did it take in seconds? "))
        corrected_time = calculator(yardstick[boat_class],race_time)
        boats.append(boat_class)
        times.append(corrected_time)
        if input("Any more boats? y/n ") == 'n':
            add_boat = False

    fastest_time = times.index(min(times))

    print("")
    for i in range(len(boats)):
        print('{:<{}} {:<{}.3f}'.format(boats[i], 10, times[i], 10))

    if len(boats) > 1:
        print(f"\n-- {boats[fastest_time]} WINS --") 

    input("\n\nPress enter to restart")
    portsmouth()

portsmouth()