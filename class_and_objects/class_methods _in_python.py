#class methods in python
class New:
    def __init__(self):
        print('constructor is created')
    @classmethod
    def sathya(self):
        print('hello we are inside class method')
    @staticmethod
    def hash():
        print('inside static method')
    
obj = New()
obj.sathya()
obj.hash()