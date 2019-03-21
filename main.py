import datetime, numpy, configparser
import matplotlib.pyplot as plt

Config = configparser.ConfigParser()
Config.read('config.ini')

def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                print("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


fo = open("inputs.txt", "r")
data = eval(fo.readline())
fo.close()

if Config.read('config.ini'):
    numbofvalbs = int(ConfigSectionMap("BubbleSort")['numberofvalues'])
    stepbs = int(ConfigSectionMap("BubbleSort")['step'])
    iterationsbs = int(ConfigSectionMap("BubbleSort")['iterations'])
    numbofvalqs = int(ConfigSectionMap("QuickSort")['numberofvalues'])
    stepqs = int(ConfigSectionMap("QuickSort")['step'])
    iterationsqs = int(ConfigSectionMap("QuickSort")['iterations'])
else:
    numbofvalqs = 30000
    numbofvalbs = 30000
    stepqs = 100
    stepbs = 500
    iterationsqs = 50
    iterationsbs = 20

times = []
avges = []
xsteps = []
meantimes = []


def drawplot(x,y):
    plt.xlabel('liczba danych sortowanych n')
    plt.ylabel('czas [ms]')
    plt.title('wykres złożoności')
    plt.grid()
    plt.plot(x,y, 'ro')
    plt.show()

def average(list):
    mean = numpy.mean(list, axis=0)
    sd = numpy.std(list, axis=0)

    final_list = [x for x in list if (x > mean - 2 * sd)]
    final_list = [x for x in final_list if (x < mean + 2 * sd)]
    try:
        av = sum(final_list) / len(final_list)
        avges.append(int(av))
        return int(av)
    except ZeroDivisionError:
        av = sum(list) / len(list)
        return int(av)





def saveoutputs(list, opt, n):
    if opt == 1:
        fo = open("BS_wy.txt", "a") 
        fo.write("N = {}: \n".format(n))
        fo.writelines(str(list))
        fo.write('\n')
        fo.write('Sredni czas: {}ms\n'.format(aver))
        fo.write('___________________________________\n')

        fo.close()

    elif opt == 2:
        fo = open("QS_wy.txt", "a") 
        fo.write("N = {}: \n".format(n))
        fo.writelines(str(list))
        fo.write('\n')
        fo.write('Sredni czas: {}ms\n'.format(aver))
        fo.write('___________________________________\n')

        fo.close()



def bubblesort(list, numofval):
    start = datetime.datetime.now()
    for num in range(numofval-1, 0, -1):
        for i in range(0, num):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
    duration = datetime.datetime.now() - start
    times.append(int(duration.total_seconds() * 1000))


def quicksort(arr, l=0, r=None):
    if r is None: r = len(arr) - 1
    i, j = l, r
    if (l+r) % 2 == 0:
        mid = (l+r)/2
    else:
        mid = (l+r+1)/2
    pivot = arr[int(mid)]
    while i <= j:
        while arr[i] < pivot: i += 1
        while arr[j] > pivot: j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1; j -= 1
    if l < j: quicksort(arr, l, j)
    if r > i: quicksort(arr, i, r)






# menu
while True:
    print('''
Wybierz opcję:

1 - Bubble Sort
2 - Quick Sort
w - Wyjście''')
    inp = str(input())
    if inp == '1':
        fo = open("inputs.txt", "r")
        data = eval(fo.readline())
        fo.close()
        print("Trwa sortowanie...")
        for j in range(0, numbofvalbs+stepbs, stepbs):
            for i in range(iterationsbs):
                bubblesort(data, j)
            xsteps.append(j)
            aver = average(times)
            saveoutputs(times, 1, j)
            meantimes.append(aver)
            times.clear()
        drawplot(xsteps, meantimes)

    elif inp == '2':
        print("Trwa sortowanie...")
        fo = open("inputs.txt", "r")
        data = eval(fo.readline())
        fo.close()
        #print(data)

        for j in range(0, numbofvalqs+stepqs, stepqs):
            for i in range(iterationsqs):
                startTime = datetime.datetime.now()
                quicksort(data, 0, j-1)
                duration = datetime.datetime.now() - startTime
                times.append(int(duration.total_seconds() * 1000))
                #print(data2)
            xsteps.append(j)
            #print(times)
            aver = average(times)
            saveoutputs(times, 2, j)
            meantimes.append(aver)
            times.clear()
        drawplot(xsteps, meantimes)
        #print(data)




    elif inp == 'w':
        break
    else:
        print('Nie ma takiej opcji!')
        continue

'''        while True:
            print("Podaj ile elementów chcesz posortować: ")
            numofval = input()
            if numofval.isnumeric():
                if int(numofval) < len(data)+1:
                    for i in range(10):
                        bubblesort(data,int(numofval))
                    break
                else:
                    print('Zła wartość!')
            else:
                print('Musisz wpisać liczbę!')
'''
