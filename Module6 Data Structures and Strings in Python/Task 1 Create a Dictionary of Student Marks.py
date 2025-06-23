dict = {'maria':230,'ken':220, 'jonathon': 290, 'alice': 200 }
name = input('Enter the student\'s name: ')
if name in dict:
    print(f'{name}\'s marks is {dict[name]}')
else:
    print('Student not found')