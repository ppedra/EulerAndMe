max_num = 10

possible_number = 1
while True:
    for i in range(1,max_num+1):
        if (possible_number%i==0):
            print(possible_number)
        
    possible_number+=1
    
