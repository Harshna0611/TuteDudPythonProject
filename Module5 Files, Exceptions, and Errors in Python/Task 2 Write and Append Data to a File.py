try:
    text= input(f'Enter text to write to the file: ')
    with open('output.txt','w') as file1:
        write= file1.write(f'{text}\n')
        print(f' Data successfully written to output.txt')

    text2=  input(f'\nEnter additional text to append: ')
    with open('output.txt', 'a') as file1:
        append = file1.write(text2)
    print(f'Data successfully appended')
    with open('output.txt', 'r') as file1:
        read = file1.read()
    print(f'\nFile content of output.txt:\n{read}')
except :
    print('Error: The file output.txt was not found.' )