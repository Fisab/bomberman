import window
import map
import player
import data_worker

def main():
	Window = window.Window()
	Map = map.Map(Window.cell_size, Window.screen, Window.pygame, Window.cell_amount)
	#Player = player.Hero([5,5], Window.screen, Window.pygame, Window.cell_size, Map)
	Players = data_worker.create_players(Window.screen, Window.pygame, Window.cell_size, Map)

	clock = Window.pygame.time.Clock()
	done = False

	while not done:
		for event in Window.pygame.event.get():
			if event.type == Window.pygame.QUIT:
				done = True
		#Player.query('MOVE LEFT;')
		Window.clear()
		Map.draw_map()

		for pl in Players:
			pl.query('MOVE LEFT;')
			pl.draw()

		Window.pygame.display.flip()
		clock.tick(5)
	Window.pygame.quit()

if __name__ == '__main__':
	main()