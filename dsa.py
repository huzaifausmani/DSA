# class A:
#     def __init__(self):
#         print("This is class A")
        
# class B(A):
#     def __init__(self):
#         print("This is class B")
        
# class C(A):
#     def __init__(self):
#         print("This is class C")
        
# class D(B, C):
#     def __init__(self):
#         print("D")

# obj = D()
# # no idea what python doing here.

from cryptography.fernet import Fernet

user = {'username': 'huzaifausmani', 'password': '2334011019', 'email': 'bitf19a007@pucit.edu.pk', 'img': 'UserImages\\2023-02-01_105927.038568White_Black_Simple_Initial_Logo.png', 'verfiedStatus': True, 'randomId': 8, 'Projects': []}
key = Fernet(b'fcxf3NszWl5nwy0uuntnB3BsfDz1vzKgpbA2iMQb8L8=')
print(user)
user.update(
    {'username':key.encrypt(user.get('username').encode()),
     'password':key.encrypt(user.get('password').encode()), 
     'email':key.encrypt(user.get('email').encode())}
    )
print(user)
user.update(
    {'username':key.decrypt(user.get('username')).decode(),
     'password':key.decrypt(user.get('password')).decode(), 
     'email':key.decrypt(user.get('email')).decode()}
    )
print(user)