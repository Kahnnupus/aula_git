def bubble_sort(array):
    for i in range(len(array)):
        for j in range(0,len(array) - i -1):
            if array[j] > array [j+1]:
                array[j], array [j+1] = lista[j+1], lista[j]
                print(array)
                
    return array

lista = [58,64,4,23,6,15,1]

print(bubble_sort(lista))

def gorila():
    print('''
    ▒▒▒▒▒▄██████████▄▒▒▒▒▒
    ▒▒▒▄██████████████▄▒▒▒
    ▒▒██████████████████▒▒
    ▒▐███▀▀▀▀▀██▀▀▀▀▀███▌▒
    ▒███▒▒▌■▐▒▒▒▒▌■▐▒▒███▒
    ▒▐██▄▒▀▀▀▒▒▒▒▀▀▀▒▄██▌▒
    ▒▒▀████▒▄▄▒▒▄▄▒████▀▒▒
    ▒▒▐███▒▒▒▀▒▒▀▒▒▒███▌▒▒
    ▒▒███▒▒▒▒▒▒▒▒▒▒▒▒███▒▒
    ▒▒▒██▒▒▀▀▀▀▀▀▀▀▒▒██▒▒▒
    ▒▒▒▐██▄▒▒▒▒▒▒▒▒▄██▌▒▒▒
    ▒▒▒▒▀████████████▀▒▒▒▒
        ''')