# Sort a String in decreasing order of values associated after removal of values smaller than X.

def sortMystring(str, x):
    #create list
    my_list = str.split()
    
    n = len(my_list)
    
    #remove pair whose number is less thn given number
    for i in range(n-1, 0, -2):
        if int(my_list[i])<x:
            del(my_list[i-1:i+1])
            
    n = len(my_list)
    
    #sort the given list of elements
    for i in range(1,n,2):
        for j in range(1, n-i, 2):
            if my_list[j] < my_list[j+2] or (my_list[j-1] < my_list[j+1] and my_list[j] == my_list[j+2]):
                my_list[j], my_list[j+2] = my_list[j+2], my_list[j]
                my_list[j-1], my_list[j+1] = my_list[j+1], my_list[j-1]
    return " ".join(my_list)

s = "Akshay 43 Vishva 79 dars 49 asu 98 allu 77 gansu 99"

print(sortMystring(s, 50))

    
    
