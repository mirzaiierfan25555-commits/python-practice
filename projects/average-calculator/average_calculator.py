s = 0
n = 0

print("Enter numbers to calculate average. Type 0 to stop.")

while True:
    try:
        a = int(input('Enter num: '))
        if a == 0:
            break
        s += a
        n += 1
        print('avg: ', s / n)
    except ValueError:
        print('⚠️ Error: Please enter just an integer!')
