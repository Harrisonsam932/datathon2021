from utils import Debugger

class Analyzer(object):
  def __init__(self, plotter, model):
    self.debug = Debugger()
    self.plotter = plotter
    self.model = model
    self.confusion_matrix = None
    self.specificity = None
    self.sensitivity = None
    self.bias = None
    self.variance = None
    self.precision = None
  def class_name(self):
    return "Analyzer"
  def get_confusion_matrix(self):
    return self.confusion_matrix
  def get_specificity(self):
    return self.specificity
  def get_sensitivity(self):
    return self.sensitivity
  def get_precision(self):
    return self.precision
  def get_bias(self):
    return self.bias
  def get_variance(self):
    return self.variance
  def plot_roc(self):
    pass
  def get_auc(self):
    pass
  def analyze_data(self, data):
    # Use this area as a collective "set" or "generate"
    # This should only be for storing the stats

    pass
  
class Dataset(object):
  def __init__(self):
    self.debug = Debugger()
  def class_name(self):
    return "Dataset"
  