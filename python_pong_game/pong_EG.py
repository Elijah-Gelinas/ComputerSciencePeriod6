import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Project")

color = (0, 0, 0)

FPS = 30

#rightPaddle =
#leftPaddle = 

def draw_window(left, right):
    WIN.fill(color)
    pygame.display.update()


def main():
    left = pygame.Rect(100, 250, 10, 50)
    right = pygame.Rect(800, 250, 10, 50)


    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        left.x += 1
        draw_window(left, right)
        
        
    
    pygame.quit()

if __name__ == "__main__":
    main()