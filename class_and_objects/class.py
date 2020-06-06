class Sathya:
    def __init__(self,a,b):
        self.a= a
        self.b = b
    def values(self):
        print(self.a,self.b,sep=' ')

#new = Sathya(1,2)
#print(new.a)
#print(new.b)
#new.values()
class New(Sathya):
    def __init__(self,c,d):
        Sathya.__init__(self,c,d)
        self.c = c
        self.d = d
    def new_values(self):
        print(self.c,self.d)

obj = New(5,10)
print(obj.a,obj.c)
print(obj.b,obj.d)
obj.new_values()
obj.values()

OUTPUT:
py class.py
5 5
10 10
5 10
5 10