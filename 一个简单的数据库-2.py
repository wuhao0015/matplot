# 一个简单的数据库
people = {
    'Alice': {
        'phone': '2341',
        'addr': 'Foo device 23'
     },
    'Beth': {
        'phone': '9102',
        'addr': 'Bar street 42'
     },
    'Cecil': {
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }
}
labels = {
    'phone': 'phone nubmer',
    'addr': 'address'
}
name = input('Name: ')
request = input('Phone number (p) or address (a)? ')

key = request
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')
print("{}'s {} is {}. ".format(name, label, result))
