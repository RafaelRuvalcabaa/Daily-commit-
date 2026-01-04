def suma(eggs_list) -> int:
    total = 0

    for eggs in eggs_list:
        if eggs % 2 == 0:
            total += eggs
            print(eggs)

    return total
    


eggs_list= [1,2,3,4,5,7,8,9,9,6,4,3,6,8,6,4,3,6,8,7,4,2,57,9,9]


print(suma(eggs_list))