import pygame
import random

# Hello Hello, for this exercise I decided to build my own game of snake
# because I couldent use external pictures I managed with what I have, I hope it works well!



class Snake:
    def __init__(self) -> None:
        pygame.init()

        pygame.display.set_caption("Snake")

        self.new_game()
        

        self.height = 20 #height of board
        self.width = 30 #width of board
        self.scale = 30 #size of the side of the tile squares

        self.pointIMG = pygame.image.load("coin.png")
        self.pointIMG = pygame.transform.scale(self.pointIMG, (self.scale, self.scale))

        self.window = pygame.display.set_mode((self.width * self.scale, (self.height + 1) * self.scale))
        
        self.clock = pygame.time.Clock()

        self.main_loop()


    def new_game(self):
        self.direction = "right" #default direction
        self.body = [(10,10)] #default position
        self.point = (15, 15) #position of first point
        self.score = 0 #game score
        self.death = False #flag for when game is over
        self.game_font = pygame.font.SysFont("Arial", 20)

    def main_loop(self):
        while True:
            self.check_events()
            if not self.death:
                self.move()
                self.draw_window()
                self.clock.tick(5 + (self.score))
            #what happens when game over
            else:
                self.game_font = pygame.font.SysFont("Comic Sans", 70)
                game_text = self.game_font.render("you died", True, (255, 0, 0))
                self.window.blit(game_text, (self.scale * (self.width/2 - 5), self.scale * (self.height/2 - 5)))
                pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_F2:
                    self.new_game()
                if event.key == pygame.K_LEFT:
                    if(self.direction != "right"):
                        self.direction = "left"
                elif event.key == pygame.K_RIGHT:
                    if(self.direction != "left"):
                        self.direction = "right"
                elif event.key == pygame.K_UP:
                    if(self.direction != "down"):
                        self.direction = "up"
                elif event.key == pygame.K_DOWN:
                    if(self.direction != "up"):
                        self.direction = "down"

    def move(self):
        last = self.body[-1] #remembers the position of the last body segment so i can lengthen the body if needed

        # moves the body segments forward
        for index in range(len(self.body) - 1, -1, -1):
            if(index > 0):
                self.body[index] = self.body[index - 1]

        # moves the head of the snake
        if self.direction == "left":
            self.body[0] = self.body[0][0] - 1, self.body[0][1]
        if self.direction == "right":
            self.body[0] = self.body[0][0] + 1, self.body[0][1]
        if self.direction == "up":
            self.body[0] = self.body[0][0], self.body[0][1] - 1
        if self.direction == "down":
            self.body[0] = self.body[0][0], self.body[0][1] + 1

        # conditions when the game is over
        if self.body[0] in self.body[1:]:
            self.death = True
        if(self.body[0][0] < 0 or self.body[0][0] > self.width - 1):
            self.death = True
            self.body[0] = self.body[1]
        if(self.body[0][1] < 0 or self.body[0][1] > self.height - 1):
            self.death = True
            self.body[0] = self.body[1]

        # what happens when the snake gets a point
        if self.body[0] == self.point:
            self.score += 1
            self.body.append(last)
            while self.point in self.body:
                self.point = random.randint(0, self.width - 1), random.randint(0, self.height - 1)

        

    def draw_window(self):
        # delets everything
        self.window.fill((0, 0, 0))

        #drawing board lines
        for column in range(self.width):
            pygame.draw.line(self.window, (128, 128, 128), (column*30, 0), (column*30, self.height * self.scale), 1)
            pygame.draw.line(self.window, (128, 128, 128), ((column*30) + 29, 0), ((column*30) + 29, self.height * self.scale), 1)
        for row in range(self.height):
            pygame.draw.line(self.window, (128, 128, 128), (0, row*30), (self.width * self.scale, row*30), 1)
            pygame.draw.line(self.window, (128, 128, 128), (0, (row*30) + 29), (self.width * self.scale, (row*30) + 29), 1)

        #drawing snake
        pygame.draw.rect(self.window, (153, 0, 0), (self.scale * self.body[0][0], self.scale * self.body[0][1], self.scale, self.scale))
        for part in self.body[1:]:
            pygame.draw.rect(self.window, (0, 51, 102), (self.scale * part[0], self.scale * part[1], self.scale, self.scale))
        
        # drawing the point
        self.window.blit(self.pointIMG, (self.scale * self.point[0], self.scale * self.point[1]))
        
        #drawing the texts
        game_text = self.game_font.render("Score: " + str(self.score), True, (255, 0, 0))
        self.window.blit(game_text, (25, self.height * self.scale + 5))
        
        game_text = self.game_font.render("F2 = new game", True, (255, 0, 0))
        self.window.blit(game_text, (200, self.height * self.scale + 5))

        game_text = self.game_font.render("Esc = exit game", True, (255, 0, 0))
        self.window.blit(game_text, (400, self.height * self.scale + 5))

        pygame.display.flip()



Snake()
