import pygame
import sys
from settings import Settings

class KeysScreen:
	def __init__(self): 
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		self.font = pygame.font.Font(self.settings.font_string, self.settings.font_size)
		self.text = None
		pygame.display.set_caption("Keys")

	def run_game(self):
		while True: 
			self._check_events()
			self._update_screen()

	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				sys.exit()
			if event.type == pygame.KEYDOWN: 
				self._print_to_screen(event)

	def _print_to_screen(self, event): 
		self.text = self.font.render(pygame.key.name(event.key) , True, (0,0,0), (255,255,255))


	def _update_screen(self): 
		self.screen.fill(self.settings.bg_color)
		if self.text != None :
			text_rect = self.text.get_rect()
			text_rect.center = self.screen.get_rect().center
			self.screen.blit(self.text, text_rect)
		pygame.display.flip()

if __name__ == "__main__": 
	ks = KeysScreen()
	ks.run_game()