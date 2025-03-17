class Cookie:
    ##constructor
    def __init__(self, color):
        self.color = color
    
    #no arguements passed
    def get_color(self):
        return self.color
    
    #color passed so change korbe
    def set_color(self, color):
        self.color = color


cookie_one = Cookie('green')      
cookie_two = Cookie('blue')  

print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())

cookie_two.set_color('red')

print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())
