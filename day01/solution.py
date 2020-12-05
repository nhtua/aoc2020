numbers = open('input.txt', 'r').readlines()


for i in range(0, len(numbers)):
    for j in range(i, len(numbers)):
        a = int(numbers[i])
        b = int(numbers[j])
        if a+b == 2020:
            print("Result: %d x %d = %d" % (a, b, a*b))

for i in range(0, len(numbers)):
    for j in range(i, len(numbers)):
        for h in range(j, len(numbers)):
            a = int(numbers[i])
            b = int(numbers[j])
            c = int(numbers[h])
            if a+b+c == 2020:
                print("Result: %d x %d x %d = %d" % (a, b, c, a*b*c))


