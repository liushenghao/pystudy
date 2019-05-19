def mySort(list2,reverse=0):
    i=len(list2)
    if not reverse:
        while(i>1):
            j=0
            while(j<i-1):
                if(list2[j]>list2[j+1]):
                    list2[j],list2[j+1]=list2[j+1],list2[j]
                j=j+1
            i=i-1
    else:
        while(i>1):
            j=0
            while(j<i-1):
                if(list2[j]<list2[j+1]):
                    list2[j],list2[j+1]=list2[j+1],list2[j]
                j=j+1
            i=i-1
    return list2

list1 = input()
list2 = mySort(list(map(int,list(list1))),reverse=1)
print(list2)
