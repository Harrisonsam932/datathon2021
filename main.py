from visualize import Plotter
from utils import ImageManager
from guis import GUI
from analyze import Analyzer
from model import Modeller

def gen_plot():
  plotter.add_x_val(range(-10,11)) # [-2, -1, 0, 1, 2]
  plotter.add_y_val(map(lambda x : x ** 2, range(-10,11))) # [4,1,0,1,4]

  plotter.save()
  plotter.close()

  image_manager.scale('plot.png', 'plot.png', 250)

plotter = Plotter()
image_manager = ImageManager()
gui = GUI()
#analyzer = Analyzer()
#modeller = Modeller()

gen_plot()

gui.text('MatPlotLib Figure')
gui.next()
gui.image('plot.png')
gui.next()
gui.button('Exit')

gui.compile()
gui.loop()
gui.close()