import math
import random
import config as g
from PIL import Image

class Randomizer(object):
  def __init__(self):
    random.seed()
  def random_list(self, size, lower, upper):
    data = []
    for i in range(size):
      data.append(random.randint(lower, upper))
    return data

class Globals(object):
  def __init__(self):
    pass

class Math(object):
    def __init__(self):
        pass
    def class_name(self):
        return 'Math'
    def quadrature(self, a, b):
        return math.sqrt(a**2 + b**2)
    def ss(self, function, vals):
        sum = 0
        for val in vals:
          sum += self.function(val)
        return sum

class Debugger(object):
    def __init__(self):
        self.level = g.debug_level
    def class_name(self):
        return 'Debugger'
    def prn(self, obj, msg, level=2):
        if not self.level == 0:
            if level <= self.level:
                print(f'<{obj.class_name()}>:\t\t{msg}')

class ImageManager(object):
    def __init__(self):
        self.debug = Debugger()
        self.debug.prn(self, 'ImageManager object created.')
    def class_name(self):
        return 'ImageManager'
    def scale(self, file_in, file_out, baseheight):
        img = Image.open(file_in)
        hpercent = (baseheight / float(img.size[1]))
        wsize = int((float(img.size[0]) * float(hpercent)))
        img = img.resize((wsize, baseheight), Image.ANTIALIAS)
        img.save(file_out)
        self.debug.prn(self, f'{file_in} scaled by {baseheight} to {file_out}.')