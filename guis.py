import PySimpleGUI as sg

from utils import Debugger

from os import path

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
  def __init__(self, plotter, analyzer, modeller):
    self.is_compiled = False
    self.title = None
    self.layout = [[]]
    self.row = 0
    self.theme = None
    self.debug = Debugger()
    self.debug.prn(self, 'GUI object created.')
    self.submit_func = None
    self.plot_shown = 'plot.png'
    self.plotter = plotter
    self.analyzer = analyzer
    self.modeller = modeller
  def class_name(self):
    return 'GUI'
  def standard(self):
    self.text('MatPlotLib Figure')
    self.next()
    self.image(self.plot_shown)
    self.next()
    self.text('Show: ')
    self.input('Show')
    self.next()
    self.button('Exit')
    self.button('Submit')
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
  def loop(self):
    if self.is_compiled:
      while True:
        event, values = self.window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
          self.debug.prn(self, 'Exit triggered.')
          break
        if event == 'Submit':
          if values['Show'].count(':') == 1:
            header = values['Show'].split(':')[0]
            body = values['Show'].split(':')[1]
            if header == 'i':
              if path.exists(f'imgs/{body}.png'):
                self.debug.prn(self, 'Updating visible file.')
                self.close()
                self.plot_shown = f'imgs/{body}.png'
                self.clear()
                self.standard()
                self.compile()
                self.loop()
                self.close()
              else:
                self.debug.prn(self, 'File does not exist.', 1)
            elif header == 'v':
              text = ''
              if body == 'ls-a' or body == 'ls-slope':
                text = f'slope = {self.modeller.linear(0).get_slope()}'
              elif body == 'ls-b' or body == 'ls-yint':
                text = f'yint = {self.modeller.linear(0).get_yint()}'
              elif body == 'specif':
                text = f'specificity = {self.analyzer.get_specificity()}'
              elif body == 'sensit':
                text = f'sensitivity = {self.analyzer.get_sensitivity()}'
              elif body == 'precis':
                text = f'precision = {self.analyzer.get_precision()}'
              elif body == 'acc':
                text = f'accuracy = {self.analyzer.get_accuracy()}'
              elif body == 'recall':
                text = f'recall = {self.analyzer.get_recall()}'
              elif body == 'fout':
                text = f'fallout = {self.analyzer.get_fallout()}'
              elif body == 'bias':
                text = f'bias = {self.analyzer.get_bias()}'
              elif body == 'var':
                text = f'variance = {self.analyzer.get_variance()}'
              elif body == 'cm':
                text = f'confusion matrix = {self.analyzer.get_confusion_matrix()}'
              elif body == 'auc':
                text = f'auc = {self.analyzer.get_auc()}'
              else:
                self.debug.prn(self, 'Variable could not be found.', 1)
                continue
              self.debug.prn(self, f'Popping up {body} variable.')
              popup = PopUp('Accessor')
              popup.set_text(text)
              popup.show()
              popup.loop()
              popup.close()
            else:
              self.debug.prn(self, 'Unknown header.', 1)
          else:
            self.debug.prn(self, 'Must use exactly 1 colon (:).', 1)
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

class PopUp(object):
  def __init__(self, title):
    self.text = None
    self.debug = Debugger()
    self.title = title
  def class_name(self):
    return 'PopUp'
  def get_text(self):
    return self.text
  def set_text(self, text):
    self.text = text
    self.debug.prn(self, 'Text set.')
  def show(self):
    self.layout = [
      [sg.Text(self.text)],
      [sg.Button('OK')]
    ]
    self.window = sg.Window(self.title, self.layout)
    self.debug.prn(self, 'Message shown.')
  def loop(self):
    self.debug.prn(self, 'Loop commenced.')
    while True:
        event, values = self.window.read()
        if event == 'OK' or event == sg.WIN_CLOSED:
          self.close()
          break
  def close(self):
    self.window.close()
    self.debug.prn(self, 'Message terminated.')