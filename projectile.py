import pygame
 
class Projectile(pygame.sprite.Sprite):
	
	def __init__(self, player):
		super().__init__()
		self.velocity = 5
		self.player = player
		self.image = pygame.image.load("images/bomb.png")
		self.image = pygame.transform.scale(self.image, (40, 40))
		self.rect = self.image.get_rect()
		self.rect.x = player.rect.x + 70
		self.rect.y = player.rect.y + 50
		self.origin_image = self.image
		self.angle = 0
		self.bomb_sound = pygame.mixer.Sound("sounds/bomb.wav")

	def rotate(self):
		self.angle += 2
		self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
		self.rect = self.image.get_rect(center = self.rect.center)
		
	def remove(self):
		self.player.all_projectiles.remove(self)
	
	def move(self):
		self.rect.x += self.velocity
		self.rotate()
		
		for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
			self.remove()
			monster.damage(self.player.attack)
			self.bomb_sound.set_volume(0.5)
			self.bomb_sound.play()
		
		if self.rect.x > 1000:
			self.remove()
			
