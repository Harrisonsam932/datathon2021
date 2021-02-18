from utils import Debugger

class Modeller(object):
  def __init__(self, analyzer):
    self.debug = Debugger()
    self.analyzer = analyzer
    self.data = None
  def class_name(self):
    return "Modeller"
  def set_data(self, data):
    self.data = data
  def get_data(self):
    return self.data
  def rm_data(self):
    self.data = None
  def plot_sum_of_squares_residuals(self, slopes):
    pass
  
class Model(object):
   pass

class LeastSquaresModel(Model):
  def __init__(self, slope, yint):
    self.slope = None
    self.yint = None
  def __del__(self):
    del self.slope
    del self.yint
  def class_name(self):
    return "LeastSquaresModel"
  def get_slope(self):
    return self.slope
  def get_yint(self):
    return self.yint
  def get_sum_of_sqauared_residuals(self):
    pass

class LogisticModel(Model):
  pass