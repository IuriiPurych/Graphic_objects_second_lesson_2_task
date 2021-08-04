class Rectangle:
    x = int
    y = int
    height_rectangle = int
    length_rectangle = int

    def __init__(self, x, y, height, length):
        self.x = x
        self.y = y
        self.height_rectangle = height
        self.length_rectangle = length

    def draw_rectangle(self):
        print(f'The rectangle with height: {self.height_rectangle} and length: {self.length_rectangle} was drawn.')


class Button(Rectangle):
    text = str

    def __init__(self, x, y, height, length, text='button'):
        Rectangle.__init__(self, x, y, height, length)
        self.text = text

    def draw_button(self):
        Rectangle.draw_rectangle(self)
        print(f'{self.text}')

    def on_click(self):
        print(f'The button: {self.text} was clicked.')


b = Button(1, 2, 5, 10, 'Кнопка')
b.draw_button()
b.on_click()