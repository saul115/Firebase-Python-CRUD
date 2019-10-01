from firebase import firebase

firebase = firebase.FirebaseApplication("https://python-crud-b6b7f.firebaseio.com/",None)

firebase.delete('/python-crud-b6b7f/Customer','/-Lq55uWmhbvzz0Vq81O1')
print('Delete Succesfully')
