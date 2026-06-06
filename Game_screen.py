import pygame
pygame.init()
s_width,s_height=500,500
screen=pygame.display.set_mode((s_width,s_height))
pygame.display.set_caption("Hello world.")
bg_image=pygame.transform.scale(pygame.image.load("Grey screen.jpg").convert(),(s_width,s_height))
smiley_image=pygame.transform.scale(pygame.image.load("Smiley.jpg").convert_alpha(),(300,300))
smiley_rect = smiley_image.get_rect(center=(s_width // 2,
s_height // 2 - 30))
# Initialize font, render text, and set text position
text = pygame.font.Font(None, 36).render('My first game screen', True,
pygame.Color('black'))
text_rect = text.get_rect(center=(s_width // 2, s_height // 2 + 110))
def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(bg_image, (0, 0))
        screen.blit(smiley_image, smiley_rect)
        screen.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__ == '__main__':
    game_loop()