import sys
from PySide2.QtWidgets import QApplication
from ycalc_model import YCalcModel
from ycalc_ctrl import YCalcController
from ycalc_view import YCalcView


class YCalc(QApplication):
    def __init__(self, sys_argv):
        super(YCalc, self).__init__(sys_argv)
        self.model = YCalcModel()
        self.controller = YCalcController(self.model)
        self.main_view = YCalcView(self.model, self.controller)
        self.main_view.show()


if __name__ == '__main__':
    app = YCalc(sys.argv)
    sys.exit(app.exec_())
