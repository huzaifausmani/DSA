class A:
    def __init__(self):
        print("This is class A")
        
class B(A):
    def __init__(self):
        print("This is class B")
        
class C(A):
    def __init__(self):
        print("This is class C")
        
class D(B, C):
    def __init__(self):
        print("D")

obj = D()
# no idea what python doing here.