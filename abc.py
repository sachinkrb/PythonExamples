for num in range(2,50):
    for x in range(2,num):
        if num % x == 0:
            print(str(num)+ 'not prime')
            break         
    else:
            print(str(num) + 'prime')
            
        
        
