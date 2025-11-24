class Cookie:
    def __init__(self, color):
        self.color = color
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color
        

cookie1 = Cookie("brown")
print(f"Cookie 1 color: {cookie1.get_color()}")

cookie2 = Cookie("blue")
print(f"Cookie 2 color: {cookie2.get_color()}")

cookie1.set_color("red")
print(f"Cookie 1 new color: {cookie1.get_color()}")