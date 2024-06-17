import numpy as np

def fedavg(zidian,tempmultidict):
    for k in zidian.keys():
        for i in tempmultidict.keys():
            if i == k:
                if type(zidian[k]) == list:
                    bianli3(zidian[k],tempmultidict[i]);
                    #print(temp)
                else:
                    print("进到了else里面")
                    tempmultidict[i] = zidian[k] + tempmultidict[i]


def bianli3(list1,list2):
    for i in range(len(list1)):
        for m in range(len(list2)):
            if i==m:
                print("进来了==")
                if type(list1[i]) == list:
                    bianli3(list1[i], list2[m]);
                else:
                    #print(list1[i],list2[m])
                    list2[m] = list1[i] + list2[m]
                    #print(list2[m])

