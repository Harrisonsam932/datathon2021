import PySimpleGUI as sg

from utils import Debugger

'''

layout =
[
  [text("MatPlotLib Figure")],
  [image("plot.png")],
  [button("Exit"), button("Submit")]
]

event == "Exit"

input("Name")
if event == "Name":
  if values[0] == "Ben Fedoruk":
    print("This man is a god")
  else:
    print("This is a normal man")

'''

class GUI(object):
  def __init__(self):
    self.is_compiled = False
    self.title = None
    self.layout = [[]]
    self.row = 0
    self.theme = None
    self.debug = Debugger()
    self.debug.prn(self, 'GUI object created.')
    self.submit_func = None
  def class_name(self):
    return 'GUI'
  def compile(self):
    if not self.is_compiled:
      self.window = sg.Window(self.title, self.layout)
      self.is_compiled = True
      self.debug.prn(self, 'Compiled data.')
  def set_theme(self, theme):
    sg.theme(theme)
    self.is_compiled = False
  def next(self):
    self.layout.append([])
    self.row += 1
    self.is_compiled = False
    self.debug.prn(self, f'Added row {self.row}.')
  def text(self, text):
    self.layout[self.row].append(sg.Text(text))
    self.is_compiled = False
    self.debug.prn(self, f'Added text to row {self.row}.')
  def input(self, key):
    self.layout[self.row].append(sg.InputText('', key=key))
    self.is_compiled = False
    self.debug.prn(self, f'Added input box to row {self.row}.')
  def button(self, key):
    self.layout[self.row].append(sg.Button(key))
    self.is_compiled = False
    self.debug.prn(self, f'Added button to row {self.row}.')
  def image(self, addr):
    self.layout[self.row].append(sg.Image(addr))
    self.is_compiled = False
    self.debug.prn(self, f'Added image to row {self.row}.')
  def set_title(self, title):
    self.title = title
    self.is_compiled = False
    self.debug.prn(self, 'Set title.')
  def set_submit_func(self, submit_func):
    self.submit_func = submit_func
    self.is_compiled = False
    self.debug.prn(self, 'Set submit function.')
  def loop(self):
    if self.is_compiled:
      while True:
        event, values = self.window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
          self.debug.prn(self, 'Exit triggered.')
          break
        elif event == 'Submit':
          print("Submitted!")
          self.debug.prn(self, 'Gathered data from inputs.')
    else:
      self.debug.prn(self, 'GUI not compiled.', 1)
  def clear(self):
    self.is_compiled = False
    self.title = None
    self.layout = [[]]
    self.row = 0
    self.theme = None
    self.debug.prn(self, 'GUI cleared.')
  def close(self):
    self.window.close()
    self.debug.prn(self, 'GUI closed.')