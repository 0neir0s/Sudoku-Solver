import enaml
from sudoku import *
from enaml.qt.qt_application import QtApplication
from subprocess import call

#--- Class not actually used-----
class sudokuSolution:
	inputList = [0]*81
	status = False

if __name__ == '__main__':
    with enaml.imports():
        from gui import functionView
    guiSudoku = sudokuSolution()
    app = QtApplication()
    view = functionView(sudokuSolution = guiSudoku)
    view.show()
    app.start()