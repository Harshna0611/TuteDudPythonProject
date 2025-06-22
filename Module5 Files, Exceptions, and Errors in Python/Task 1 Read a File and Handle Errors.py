try:
    with open('sample.txt','r') as file1:
        read= file1.readlines()
        print(f'Reading file content:\nLine 1: {read[0]}Line 2: {read[1]}')
except :
    print('Error: The file sample.txt was not found.' )