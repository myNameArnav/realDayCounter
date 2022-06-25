import sys

period = sys.argv[1]

if period != "help":
    time = float(sys.argv[2])

forEveryHour = 6 / 365

if period == "day":
    days2Hour = time * 24
    leapTime = round(((days2Hour + (days2Hour * forEveryHour)) / 24), 2)
    print(
        f"The actual days will be {time}, but adding the leap time it will be {leapTime}"
    )
    print(f"There will be a difference of {leapTime - time}")
elif period == "year":
    years2Hour = time * 365 * 24
    leapTime = round(((years2Hour + (years2Hour * forEveryHour)) / (365 * 24)), 2)
    print(
        f"The actual years will be {time}, but adding the leap time it will be {leapTime}"
    )
    print(f"There will be a difference of {leapTime - time}")
elif period == "plot":
    import matplotlib.pyplot as plt

    actualTime = []
    leapTime = []
    linear = []
    diff = []
    for i in range(int(round(time, 0))):
        linear.append(i)
        actualTime.append(float(i * (24)))
        leapTime.append(round(((i * (24)) + (i * forEveryHour)), 2))
        diff.append(round(((leapTime[i] - actualTime[i])), 2))
    plt.plot(actualTime, linear, label="Actual Time")
    plt.plot(leapTime, linear, label="Leap Time")
    plt.plot(diff, linear, label="Difference")
    plt.xlabel("actualTime and leapTime")
    plt.ylabel("Number of Days")
    plt.legend()
    plt.show()
elif period == "help":
    print(
        "------------\n"
        "Options\n"
        "\n"
        "day <number>: for specifying the number of day\n"
        "year <number>: for specifying number of years\n"
        "plot <number>: for plotting, in number of days\n"
        "help: you are here\n"
    )
