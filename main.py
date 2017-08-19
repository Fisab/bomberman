import window
import map
import player

def main():
	Window = window.Window()
	Map = map.Map(Window.cell_size, Window.screen, Window.pygame, Window.cell_amount)
	Player = player.Hero([5,5], Window.screen, Window.pygame, Window.cell_size)

	clock = Window.pygame.time.Clock()
	done = False

	while not done:
		for event in Window.pygame.event.get():
			if event.type == Window.pygame.QUIT:
				done = True

		Window.clear()
		Map.draw_map()
		Player.draw()
		Window.pygame.display.flip()
		clock.tick(3)
	Window.pygame.quit()

if __name__ == '__main__':
	main()