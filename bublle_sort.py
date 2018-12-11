sales = [50,54,29,33,22,100,45,54,89,75]



def sort_high_to_low():
    for _passagem in range(0,len(sales)):
        done_swap = False
        for count in range(0,len(sales)-1-_passagem):
            if sales[count] < sales[count+1]:
                bucket = sales[count]
                sales[count] = sales[count+1]
                sales[count+1] = bucket
                done_swap = True
                print(sales)
        if done_swap == False:
            break

               

    #print(sales)

sort_high_to_low()

