import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from ycalc_ui import Ui_MainWindow
from abc import ABC, abstractmethod
import yobit_api


class YCalc(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.operation = self.check_direction()

        self.ui.currencyBox.currentIndexChanged[int].connect(self.change_currency)
        self.ui.directionBox.currentIndexChanged[int].connect(self.change_direction)
        self.ui.refreshButton.clicked.connect(self.refresh_rate)
        self.ui.calculateButton.clicked.connect(self.calculate)

    def check_direction(self):
        """ Создание экземпляра нужного класса в зависимости от направления обмена
        """
        direction = self.ui.directionBox.currentIndex()
        if direction == 0:
            return Buy(self.ui)
        elif direction == 1:
            return Sale(self.ui)
        # else:
            # TODO: бросить исключение

    def change_direction(self):
        self.operation = self.check_direction()

    def change_currency(self):
        self.operation.set_currency()

    def calculate(self):
        self.operation.calculate_btn()

    def refresh_rate(self):
        self.operation.refresh_btn()


class Operation(ABC):

    KEY = None

    def __init__(self, ui):
        self.ui = ui

    def get_currency_box(self):
        return self.ui.currencyBox.currentText()

    @abstractmethod
    def set_currency(self):
        pass

    def refresh_btn(self):
        pair = self.get_currency_box().lower() + "_usd"
        response = yobit_api.PublicApi().get_pair_ticker(pair=pair)
        self.ui.rateInput.setText('%.8f' % response[self.KEY])

    @abstractmethod
    def calculate_btn(self):
        pass


class Buy(Operation):
    """ Направление - покупка криптовалюты
    """
    KEY = 'sell'

    def __init__(self, ui):
        super().__init__(ui)
        self.ui.giveInput.setText('%.8f' % 0)
        self.ui.giveCurLabel.setText('USD')
        self.ui.commissionInput.setText('0.2')
        self.ui.commissionCurLabel.setText('%')
        self.ui.commissionMoneyInput.setText('%.8f' % 0)
        self.ui.commissionMoneyCurLabel.setText('USD')
        self.ui.netLabel.setText('Отдаю - Ком.:')
        self.ui.netInput.setText('%.8f' % 0)
        self.ui.netCurLabel.setText('USD')
        self.ui.rateInput.setText('%.8f' % 0)
        self.ui.rateCurLabel.setText('USD')
        self.ui.receiveInput.setText('%.8f' % 0)
        self.ui.receiveCurLabel.setText(self.get_currency_box())
        self.ui.netInput.setReadOnly(True)
        self.ui.receiveInput.setReadOnly(True)

    def set_currency(self):
        self.ui.receiveCurLabel.setText(self.get_currency_box())

    def calculate_btn(self):
        give = float(self.ui.giveInput.text())
        commission = float(self.ui.commissionInput.text())
        commission_money = give/100.2 * commission
        self.ui.commissionMoneyInput.setText('%.8f' % commission_money)
        net = give - commission_money
        self.ui.netInput.setText(str('%.8f' % net))
        rate = float(self.ui.rateInput.text())
        if not rate:
            receive = 0
        else:
            receive = net / rate
        self.ui.receiveInput.setText(str('%.8f' % receive))


class Sale(Operation):
    """ Направление - продажа криптовалюты
    """
    KEY = 'buy'

    def __init__(self, ui):
        super().__init__(ui)
        self.ui.giveInput.setText('%.8f' % 0)
        self.ui.giveCurLabel.setText(self.get_currency_box())
        self.ui.commissionInput.setText('0.2')
        self.ui.commissionCurLabel.setText('%')
        self.ui.commissionMoneyInput.setText('%.8f' % 0)
        self.ui.commissionMoneyCurLabel.setText('USD')
        self.ui.netLabel.setText('Получаю + Ком.:')
        self.ui.netInput.setText('%.8f' % 0)
        self.ui.netCurLabel.setText('USD')
        self.ui.rateInput.setText('%.8f' % 0)
        self.ui.rateCurLabel.setText('USD')
        self.ui.receiveInput.setText('%.8f' % 0)
        self.ui.receiveCurLabel.setText('USD')
        self.ui.netInput.setReadOnly(True)
        self.ui.receiveInput.setReadOnly(True)

    def set_currency(self):
        self.ui.giveCurLabel.setText(self.get_currency_box())

    def calculate_btn(self):
        give = float(self.ui.giveInput.text())
        commission = float(self.ui.commissionInput.text())
        rate = float(self.ui.rateInput.text())
        gross = give * rate
        self.ui.netInput.setText(str('%.8f' % gross))
        commission_money = gross/100 * commission
        self.ui.commissionMoneyInput.setText('%.8f' % commission_money)
        receive = gross - commission_money
        self.ui.receiveInput.setText(str('%.8f' % receive))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ycalc = YCalc()
    ycalc.show()
    sys.exit(app.exec_())
