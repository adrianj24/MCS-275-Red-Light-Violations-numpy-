import numpy as np
import datetime
import matplotlib.pyplot as plt

# Problem 1

def Month(d):
    M = {}
    with open(d, 'r') as f:
        for line in f:
            if not line.startswith('INTERSECTION'):
                L = line.split(",")
                date = L[3].split("/")
                month = int(date[0])
                viol = int(L[4])
                if month not in M:
                    M.update({month:viol})
                else:
                   M[month] = M[month] + viol
    
    return(M)

    
                    
def PlotGraph(M):
    print(M)
    months = []
    viols = []
    for month in M:
        months.append(month)
        viols.append(M[month])

    x = np.array(months)
    y = np.array(viols)
    f = np.polyfit(x, y, 1)
    F = np.poly1d(f)
    print("Fitted Linear Function: ", F)
    X = np.linspace(-5, 15, 70)
    Y = F(X)
    plt.plot(x, y, 'bo', X, Y, 'r--')
    plt.xlim(0,13)
    plt.ylim(100000, 230000)
    plt.legend(['Data Points', 'Fitted Curve F(X)'])
    plt.xlabel('Months')
    plt.ylabel('Number of Red Light Violations')
    plt.grid()
    plt.show()


def main():
    Data = Month('D:\Downloads\mcs 275 proj 2 data.csv')
    PlotGraph(Data)

main()

#Problem 2

def days(b):
    D = {}
    with open(b, 'r') as f:
        for line in f:
            if not line.startswith("INTERSECTION"):
                L = line.split(",")
                a = datetime.datetime.strptime(L[3], '%m/%d/%Y').strftime('%Y, %m, %d')
                b = [x.strip() for x in a.split(',')]
                year = int(b[0])
                month = int(b[1])
                day = int(b[2])
                day_num = datetime.date(year, month, day).isoweekday()
                viol = int(L[4])
                if day_num not in D:
                    D.update({day_num:viol})
                else:
                    D[day_num] = D[day_num] + viol

    return(D)


def PlotGraph2(D):
    print(D)
    months = []
    viols = []
    for day_num in D:
        months.append(day_num)
        viols.append(D[day_num])

    x = np.array(months)
    y = np.array(viols)
    f = np.polyfit(x, y, 7)
    F = np.poly1d(f)
    print("Fitted Linear Function: ", F)
    X = np.linspace(-5, 15, 70)
    Y = F(X)
    plt.plot(x, y, 'bo', X, Y, 'r--')
    plt.xlim(0, 8)
    plt.ylim(220000, 310000)
    plt.legend(['Data Points', 'Fitted Curve F(X)'])
    plt.xlabel('Days')
    plt.ylabel('Number of Red Light Violations')
    plt.grid()
    plt.show()

def main2():
    Data = days('mcs 275 proj 2 data.csv')
    PlotGraph2(Data)

main2()
