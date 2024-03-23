import pygame
import random

class Heart(pygame.sprite.Sprite):

	def __init__(self, life):
		super().__init__()
		self.image = pygame.image.load("images/heart.png")
		self.rect = self.image.get_rect()
		self.image = pygame.transform.scale(self.image, (50, 50))
		self.velocity = 1
		self.rect.x = random.randint(0, 900)
		self.rect.y = - random.randint(0, 800)
		self.life = life
		self.heart_sound = pygame.mixer.Sound("sounds/heart.wav")
	
	def remove(self):
		self.life.all_hearts.remove(self)
	
	def fall(self):
		self.rect.y += self.velocity
		if self.rect.y >= 500:
			self.remove()

		if self.life.game.check_collision(self, self.life.game.all_players):
			self.remove()
			self.life.game.player.save(10)
			self.heart_sound.set_volume(1.0)
			self.heart_sound.play()
			print("You won a heart!!")
