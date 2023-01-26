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
password = "2334011019huzaifa"
key = Fernet(b'fcxf3NszWl5nwy0uuntnB3BsfDz1vzKgpbA2iMQb8L8=')
encrypted = key.encrypt(password.encode())
print(encrypted)
decrypted = key.decrypt(encrypted).decode()
print(decrypted)
