from firebase import firebase

firebase = firebase.FirebaseApplication("https://python-crud-b6b7f.firebaseio.com/",None)

firebase.put("/python-crud-b6b7f/Customer/-Lq59eQYil-ictnQVnqE",'Name','Augusto Gasca Farrera')
print('Update Succesfully')