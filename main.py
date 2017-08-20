import window
import map
import player
import data_worker
import bomb
import tools

def main():
	Window = window.Window()
	Map = map.Map(Window.screen, Window.pygame)

	players = data_worker.create_players(Window.screen, Window.pygame, Map)
	Data = data_worker.Data(Map.blocks, players)

	for i in players:
		i.Data = Data

	clock = Window.pygame.time.Clock()
	done = False

	while not done:
		for event in Window.pygame.event.get():
			if event.type == Window.pygame.QUIT:
				done = True
		Data.update()
		Window.clear()
		for pl in players:
			pl.update()

		Map.draw_map()
		for pl in players:
			pl.draw()

		Window.pygame.display.flip()
		clock.tick(3)
	Window.pygame.quit()

if __name__ == '__main__':
	main()