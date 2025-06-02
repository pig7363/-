class Bird:
    def fly(self):
        raise NotImplementedError
    
class Eagle(Bird):
    def fly(self):
        print("펄럭펄럭")

a=Eagle()
a.fly()