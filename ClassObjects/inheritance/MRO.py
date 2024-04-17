class A:
    # def meth_1(self):
    #     print("Welcome")
    pass



class C(A):
    def meth_1(self):
        print("Hello")
        
class B(C,A):
    # def meth_1(self):
    #     print("Hi")
    pass
        
class D(B):
    pass

d = D()
d.meth_1()

