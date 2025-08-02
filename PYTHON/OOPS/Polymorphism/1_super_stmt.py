#super(): This stmt is used  to call super class methods or constructor through 
#sub class method or constructor 

class A: 
    def __init__(self):
        print('form consturctor A...')
        self.x = 10 

class B(A):
    def __init__(self):
        print('constructor from class B')
        super().__init__() #executes super class constructor 
        self.y=20 
        print(self.x)
        print(self.y)


b1 = B()

#here first super class constructor executes followed by sub class constructor 
#here both logics are executed userdefined logic(derived class logic) and base class logic 

