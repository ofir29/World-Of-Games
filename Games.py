def boom(x, boom_num):
    numbers = range(1, x)
    for number in numbers:
        if number % boom_num == 0 or str(boom_num) in str(number):
            print("BOOM!")
        else:
            print(number)

boom(100, 7)
