'''
Author: Vinicius H. Higa

'''

while True:
    coords = input()

    array = coords.split(' ')

    if array[0] == '0' and array[1] == '0' and array[2] == '0' and array[3] == '0':
        break
    
    # If it is in the same position
    if array[1] == array[3] and array[0] == array[2]:
        print('0')
    # Or if it is in the same row
    elif array[1] == array[3]:
        print('1')
    # Or if it is in the same column
    elif array[0] == array[2]:
        print('1')
    # Verifying the diagonals...
    else:
        x1 = int(array[0])
        y1 = int(array[1])
        x2 = int(array[2])
        y2 = int(array[3])

        if abs(x1 - x2) ==  abs(y1 - y2):
            print('1')
        else:
            print('2')