import pygame

class Firework(object):
    def __init__(self, x_pos):
        # loading firework
        self.state = "ALIVE"
        self.y = 400
        self.x = x_pos
        self.speed = 10
        self.destination = 100
        self.color = (255, 0, 0)
        self.circle_size = 0
        self.countdown = 0

    def update(self):
        if self.countdown > 0:
            self.countdown -= 1
            return

        if self.state == "ALIVE":
            self.y -= self.speed
            if self.y < self.destination:
                self.state = "EXPLODING"
        elif self.state == "EXPLODING":
            self.circle_size += 1
            if self.circle_size > 20:
                self.state = "DEAD"
        elif self.state == "DEAD":
            # Finished exploding - so reset
            self.countdown = 10
            self.y = 400
            self.circle_size = 0
            self.state = "ALIVE"

    def draw(self, screen):
        pygame.draw.line(screen, self.color, (self.x -1, self.y -1), (self.x + 1 , self.y + 1))
        pygame.draw.line(screen, self.color, (self.x +1, self.y -1), (self.x - 1 , self.y + 1))

        if self.state == "EXPLODING":
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.circle_size)