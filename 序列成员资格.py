database = [
['hale', '12345'],
['cisco', '23456'],
['python', '34567']
]
username = input('User Name: ')
pin = input('PIN code: ')
if [username, pin] in database:
    print('Access Granted!')
else:
    print('Access Denied!')
