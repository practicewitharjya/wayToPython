# Hybrid Interitance

class A:
    def Asound(self):
        print("It is A's sound")

class B(A):
    def Bsound(self):
        print("It is B's sound")

class C(A):
    def Csound(self):
        print("It is C's sound")

class D(B, C):
    def Dsound(self):
        print("It is D's sound")


d = D()
d.Asound()