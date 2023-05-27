def main():
    people, index, number = 30,0,0
    list1 = [True]*people
    while people >15:
        if list1[index]:
            number+=1
            if number == 9:
                list1[index]=False
                people-=1
                number =0
        index+=1
        index%=30
    for i in range(people):
        if list1[i]:
            print('%d'%(i+1))
if __name__ == "__main__":
    main()
        
        