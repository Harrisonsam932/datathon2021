import matplotlib
import matplotlib.pyplot as plt

from utils import Constants
from utils import Debugger

class Plotter(object):
  def __init__(self):
    self.c = Constants()
    self.debug = Debugger()
    self._set_axes()
    self._set_labels()
    self.x_vals = []
    self.y_vals = []
    self.debug.prn(self, 'Plotter object created.')
  def class_name(self):
    return 'Plotter'
  def load(self, x_vals, y_vals):
    self.x_vals = x_vals
    self.y_vals = y_vals
    self.debug.prn(self, 'Values added to Plotter.')
  def _set_axes(self):
    plt.axhline(0, color=self.c.get_x_clr())
    plt.axvline(0, color=self.c.get_y_clr())
    self.debug.prn(self, 'Axes drawn.', 3)
  def _set_labels(self):
    plt.xlabel(self.c.get_x_lbl())
    plt.ylabel(self.c.get_y_lbl())
    self.debug.prn(self, 'Labels set.', 3)
  def plot(self):
    if len(self.x_vals) == len(self.y_vals):
      plt.plot(self.x_vals, self.y_vals)
      self.debug.prn(self, 'Plot drawn.')
      plt.show()
    else:
      self.debug.prn(self, f'x_vals({len(self.x_vals)}) and y_vals({len(self.y_vals)}) must be of same length.', 1)
  def save(self):
    if len(self.x_vals) == len(self.y_vals):
      plt.plot(self.x_vals, self.y_vals)
      self.debug.prn(self, 'PNG image saved.')
      plt.savefig('plot.png')
    else:
      self.debug.prn(self, f'x_vals({len(self.x_vals)}) and y_vals({len(self.y_vals)}) must be of same length.', 1)
  def get_x_vals(self):
    return self.x_vals
  def get_y_vals(self):
    return self.y_vals
  def add_x_val(self, x):
    for v in x:
      self.x_vals.append(v)
    self.debug.prn(self, 'X values added.')
  def add_y_val(self, y):
    for v in y:
      self.y_vals.append(v)
    self.debug.prn(self, 'Y values added.')
  def close(self):
    plt.close()
    self.debug.prn(self, 'Plot closed.')