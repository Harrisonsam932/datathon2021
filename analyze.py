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

# TP -- true pos, TN -- true neg, FP -- false pos, FN -- false neg
# Likes cocacola growing up?
# You will become an achoholic
# specificity = TP / (TP + FP)
# sensitivity = TN / (TN + FN)

'''

specificity
|
|
|
|
|
-------------------
(1-sensitivity)

'''
  
class Dataset(object):
  def __init__(self):
    self.debug = Debugger()
  def class_name(self):
    return "Dataset"
  
'''

[(x1,y1),(x2,y2),(x3,y3)...]
y=ax+bz+c
[(x1,z1,y1),(x2,z2,y2)...]
[(x1,x2,x3...), (y1,y2,y3...), (z1,z2,z3...)]

'''

(weight_mouse, age, height, length, parents, location, diet, bodymassindex)

#<!-----Task Board-----!>#

# Russell --> SQL
# Kai     --> Dataset
# Harry   --> Analyzer
# Ben     --> Models

# Tasks:
# Dataset hooked up w visualize. 
# Analyzer
# Models