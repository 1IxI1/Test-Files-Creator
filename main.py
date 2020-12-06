import os.path
import time
from progress.bar import Bar

os.system("cls||clear")

if os.path.exists("file.txt"):
    os.remove("file.txt")

open('file.txt', 'tw', encoding='utf-8')
f = open('file.txt', 'r+')

n = 12

def steps():

    global n

    print('')

    n = input('Select count of process steps (Default 12): ')

    if n == '':
    	n = 12
    else:
        try:
            n = int(n)
        except:
            print('Please, try again')
            steps()

type = int(input('0) Tb    1) Gb    2) Mb    3) Kb\n\nSize in: '))
steps()

if type == 0:
    stroke = 'o' * (int(input('\nSize (number): ')) * int((2 ** 40)/n))
elif type == 1:
        stroke = 'o' * (int(input('\nSize (number): ')) * int((2 ** 30)/n))
elif type == 2:
        stroke = 'o' * (int(input('\nSize (number): ')) * int((2 ** 20)/n))
elif type == 3:
        stroke = 'o' * (int(input('\nSize (number): ')) * int((2 ** 10)/n))

print()

with Bar('Creating file', max=n) as bar:
    for i in range(n):
        f.write(stroke)
        bar.next()

time.sleep(1)
print("\nDone")
time.sleep(1)

f.close()
