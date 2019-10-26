#!/data/data/com.termux/files/usr/bin/python

import statistics
from os import system

try:
    lis = []
    print("-" * 50)
    data = str(input("Masukkan data: "))
    datalist = data.split(",")
    for i in datalist:
        lis.append(int(i))

    urut = lis.sort()
    mean = statistics.mean(lis)
    median = statistics.median(lis)
    modus = statistics.mode(lis)
    sd = statistics.stdev(lis)
    varian = statistics.variance(lis)
    Xmax = max(lis)
    Xmin = min(lis)
    rangenya = Xmax-Xmin

    trash = "HASIL"
    trash = trash.center(50, " ")
    print("-" * 50)
    print(trash)
    print("-" * 50)
    print("Data Urut      : {}". format(lis))
    print("Jumlah Data    : {}". format(len(lis)))
    print("Mean           : {}". format(mean))
    print("Median         : {}". format(median))
    print("Modus          : {}". format(modus))
    print("Standar Deviasi: {}". format(sd))
    print("Varian         : {}". format(varian))
    print("Range          : {}". format(rangenya))

    
except KeyboardInterrupt:
    print("CTRL-C Pressed, exiting...")
