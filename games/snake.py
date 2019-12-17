import random


class Game:
    def __init__(self):
        self.frameTime = 1
        self.startSize = 4
        self.snake = [(2, 5), (3, 5), (4, 5), (5, 5)]
        self.x_vect = 1
        self.y_vect = 0
        self.apple = (5, 5)
        self.bSize = 11
        self.running = True
        self.plant_apple()
        self.render()
        self.render_string = ""
    
    def update(self):
        if not self.running:
            return
        self.snake.append((self.snake[-1][0] + self.x_vect, self.snake[-1][1] + self.y_vect))
        snake = self.snake[-1]
        if (self.snake[-1] in self.snake[:-1] or
                snake[0] >= self.bSize or
                snake[1] >= self.bSize or
                snake[0] < 0 or
                snake[1] < 0):
            self.running = False
            self.snake.pop(0)
            return
        if self.apple not in self.snake:
            self.snake.pop(0)
        else:
            self.plant_apple()
        self.render()
    
    def plant_apple(self):
        while self.apple in self.snake:
            self.apple = (random.randint(0, self.bSize-1), random.randint(0, self.bSize-1))
    
    def render(self):
        self.render_string = ""
        for i in range(self.bSize+2):
            self.render_string += "$ "
        self.render_string += "\n"
        for y in range(self.bSize):
            self.render_string += "$ "
            for x in range(self.bSize):
                self.render_string += "@ " if self.apple == (x, y) else ("# " if (x, y) in self.snake else "  ")
            self.render_string += "$\n"
        for i in range(self.bSize+2):
            self.render_string += "$ "
