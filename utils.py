import math
from PIL import Image

class Math(object):
    def __init__(self):
        pass
    def class_name(self):
        return 'Math'
    def quadrature(self, a, b):
        return math.sqrt(a**2 + b**2)

class Constants(object):
    def __init__(self):
        self.x_clr = 'k'
        self.y_clr = 'k'
        self.x_lbl = 'X'
        self.y_lbl = 'Y'
        self.debug_level = 1
    def class_name(self):
        return 'Constants'
    def get_x_clr(self):
        return self.x_clr
    def get_y_clr(self):
        return self.y_clr
    def get_x_lbl(self):
        return self.x_lbl
    def get_y_lbl(self):
        return self.y_lbl
    def get_debug_level(self):
        return self.debug_level

class Debugger(object):
    def __init__(self):
        self.consts = Constants()
        self.level = self.consts.get_debug_level()
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