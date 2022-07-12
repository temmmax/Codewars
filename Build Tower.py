# Build Tower

def tower_builder(n_floors):
    arr_of_floors = []
    len_of_floors = n_floors * 2 - 1
    while n_floors > 0:
        space = int((len_of_floors - (n_floors*2-1))/2)
        arr_of_floors.append(' '*space+"*" * (n_floors*2-1)+' '*space)
        n_floors -= 1
    return arr_of_floors[::-1]


print(tower_builder(6))
