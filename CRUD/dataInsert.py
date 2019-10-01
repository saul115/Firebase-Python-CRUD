from firebase import firebase

firebase = firebase.FirebaseApplication("https://python-crud-b6b7f.firebaseio.com/",None)

data = {
    'Name': 'Saul Augusto Gasca Farrera',
    'Email':'sgafarrera@gmail.com',
    'Degree':'Software Enginnering' 
}

result = firebase.post('/python-crud-b6b7f/Customer',data)

print(result)
