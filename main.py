import pygame
from game import Game
import math

pygame.init()


pygame.display.set_caption("Ice Monsters")
screen = pygame.display.set_mode((1000, 700))

background = pygame.image.load("images/bg.jpg")
banner = pygame.image.load("images/banner.png")
play_button = pygame.image.load("images/play-button.png")
play_button = pygame.transform.scale(play_button, (90, 90))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/2.15)
play_button_rect.y = math.ceil(screen.get_height()/1.46)
pygame.mixer.music.load("sounds/background_music.wav")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
score = 0
font = pygame.font.Font("freesansbold.ttf", 32)

game = Game()

running = True

while running:

	screen.blit(background, (0, 0))
	
	if game.is_playing:
		game.update(screen)
		text = font.render("Score : " + str(score), True, (255, 255, 255))
		screen.blit(text, (10, 10))
	else:
		screen.blit(play_button, play_button_rect)
		screen.blit(banner, (175, 100))
		score = 0
	
	pygame.display.flip()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			print("See you soon!!")
		elif event.type == pygame.KEYDOWN:
			game.pressed[event.key] = True
			
			if event.key == pygame.K_SPACE:
				game.player.launch_projectile()
				score += 1
		elif event.type == pygame.KEYUP:
			game.pressed[event.key] = False
		
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if play_button_rect.collidepoint(event.pos):
				game.start()
				button_sound = pygame.mixer.Sound("sounds/button.wav")
				button_sound.play()
				print("All the best!!")
