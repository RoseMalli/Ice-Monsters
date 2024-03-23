import pygame
from heart import Heart

class Life:

	def __init__(self, game):
		self.percent = 0
		self.percent_speed = 5
		self.game = game
		self.all_hearts = pygame.sprite.Group()
	
	def add_percent(self):
		self.percent += self.percent_speed / 100
		
	def is_full_loaded(self):
		return self.percent >= 100
	
	def reset_percent(self):
		self.percent = 0
	
	def heart_fall(self):
		self.all_hearts.add(Heart(self))
	
	def attempt_fall(self):
		if self.is_full_loaded():
			self.heart_fall()
			self.reset_percent()		
			
	def update_bar(self, surface):
		self.add_percent()
		self.attempt_fall()
		pygame.draw.rect(surface, (0, 0, 0), [0, surface.get_height() - 20, surface.get_width(), 10])
		pygame.draw.rect(surface, (36, 197, 220), [0, surface.get_height() - 20, (surface.get_width() /100) * self.percent, 10])
