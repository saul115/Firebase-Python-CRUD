from firebase import firebase

firebase = firebase.FirebaseApplication("https://python-crud-b6b7f.firebaseio.com/",None)

result = firebase.get('/python-crud-b6b7f/Customer','')
print(result)