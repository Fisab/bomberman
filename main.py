import window
import map
import player
import data_worker

def main():
	Window = window.Window()
	Map = map.Map(Window.cell_size, Window.screen, Window.pygame, Window.cell_amount)
	players = data_worker.create_players(Window.screen, Window.pygame, Window.cell_size, Map)

	Data = data_worker.Data(Map.blocks, players)

	clock = Window.pygame.time.Clock()
	done = False

	while not done:
		for event in Window.pygame.event.get():
			if event.type == Window.pygame.QUIT:
				done = True

		Window.clear()
		Map.draw_map()

		for pl in players:
			pl.query('MOVE LEFT;')
			pl.draw()

		Window.pygame.display.flip()
		clock.tick(5)
	Window.pygame.quit()

if __name__ == '__main__':
	main()