import pygame
pygame.init()

screen = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()

player = pygame.Rect(20,170,10,60)
enemy = pygame.Rect(570,170,10,60)
ball = pygame.Rect(290,190,15,15)

bx, by = 5, 5
score1 = score2 = 0

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: 
             running = False

    keys = pygame.key.get_pressed()
    player.y += (keys[pygame.K_s] - keys[pygame.K_w]) * 5
    player.y = max(0, min(340, player.y))


    if enemy.centery < ball.centery:
          
        enemy.y += 4 

    else :
        enemy.y = -4


    ball.x += bx
    ball.y += by


    if ball.top <= 0 or ball.bottom >= 400: 
        
        by *= -1


    if ball.colliderect(player) or ball.colliderect(enemy): 
        
        bx *= -1

    if ball.left <= 0: 
        score2 += 1; 
        ball.center=(300,200); 
        bx=5

    if ball.right >= 600: 
        score1 += 1; 
        ball.center=(300,200); 
        bx=-5



    screen.fill("black")

    font = pygame.font.Font(None, 40)
    score_text = font.render(f"Player: {score1}  Opponent: {score2}", True, "white")
    screen.blit(score_text, (200, 20))


    pygame.draw.rect(screen,"white",player)
    pygame.draw.rect(screen,"white",enemy)
    pygame.draw.circle(screen,"white",ball.center,8)
    pygame.display.flip()
    clock.tick(60)



pygame.quit()
