import pygame
import random

pygame.init()

#colours
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255,255,0)
black = (0, 0, 0)



#screen

screen_width = 1200
screen_height = 600
gameWindow =pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption ("Snake game")
pygame.display.update()


#game specific var
exit_game = False
game_over = False 
snake_x = 45
snake_y = 55
init_velocity = 5
velocity_x = 0
velocity_y = 0
snk_list = []


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)



def screen_elements(text,color,x,y):
    screen_elements = font.render(text,True,color)
    gameWindow.blit(screen_elements,[x,y])

def plot_snake(gameWindow,color,snk_list,snk_size):
    for x,y in snk_list:
        pygame.draw.rect (gameWindow,color,[x,y,snk_size,snk_size])


#creating a game loop
def gameloop():
    snk_len = 1
    
    with open ("highscore.txt","r")as f:
        highscore = f.read()
    food_x = random.randint(10,screen_width-10)
    food_y = random.randint(10,screen_height-10)
    score = 0
    snk_size = 10
    fps = 60
    while not exit_game:
        if game_over:
            with open ("highscore.txt","w")as f:
                f.write(str(highscore))
            gameWindow.fill (black)
            screen_elements("game Over .!! Press enter to continue",yellow, 200 , 300)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game = True
                    exit_game 


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()


        else:

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0


            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<20 and abs(snake_y - food_y)<20:
                score +=10000
                
                food_x = random.randint(10,screen_width-10)
                food_y = random.randint(10,screen_height-10)
                snk_len +=10
                if score>int(highscore):
                    highscore = score


            gameWindow.fill(black)
            screen_elements("Score: "+str(score) + "   Highscore: "+str(highscore),red,30,30)  
            pygame.draw.rect (gameWindow,red,[food_x,food_y,snk_size,snk_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)

            snk_list.append(head)

            if len(snk_list)>snk_len:
                del snk_list [0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True

            

            #pygame.draw.rect (gameWindow,black,[snake_x,snake_y,snk_size,snk_size])
            plot_snake(gameWindow, white, snk_list, snk_size)
        pygame.display.update()
        clock.tick(fps)

            

    pygame.quit()
    quit()
gameloop()