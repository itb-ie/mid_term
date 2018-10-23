def number_times(filename, letter):
    fd = open(filename)
    times = 0
    for line in fd:
        times = times + line.count(letter)
    fd.close()
    return times


print("The letter e turns up", number_times("short.txt", "e"), "times")
