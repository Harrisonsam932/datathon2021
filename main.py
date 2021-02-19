from utils import ImageManager
from utils import Randomizer

from guis import GUI

from model import Modeller
from model import LinearModel

from analyze import Analyzer

from visualize import Plotter
from visualize import ScatterSketch
from visualize import SmoothSketch
from visualize import HistogramSketch
from visualize import VerticalLineSketch
from visualize import HorizontalLineSketch

import config as g

def gen_plot():
  plotter.set_title(g.main_graph_title)

  x = g.randomizer.random_list(25, 0, 100)
  y = g.randomizer.random_list(25, 0, 100)

  # plotter.add_x_val(x) # [-2, -1, 0, 1, 2]
  # plotter.add_y_val(y) # [4,1,0,1,4]

  scatter = ScatterSketch()
  scatter.add_x(x)
  scatter.add_y(y)
  plotter.load(scatter)

  plotter.save()
  plotter.close()

  modeller.gen_least_squares(x,y)
  analyzer.f_dist(LinearModel, plotter.save, 100)

  image_manager.scale('imgs/p.png', 'imgs/p.png', 250)

g.randomizer = Randomizer()
plotter = Plotter()
image_manager = ImageManager()
analyzer = Analyzer()
modeller = Modeller(analyzer)
gui = GUI(plotter, analyzer, modeller)

gen_plot()

#sg.theme('Dark Red 5')

gui.text('MatPlotLib Figure')
gui.next()
gui.image('imgs/p.png')
gui.next()
gui.text('Show: ')
gui.input('Show')
gui.next()
gui.button('Exit')
gui.button('Submit')

gui.compile()
gui.loop()
gui.close()