from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot, Signal
from ycalc_ui import Ui_MainWindow


class YCalcView(QMainWindow):
    currency_box = Signal(str)
    direction_box = Signal(str)

    def __init__(self, model, controller):
        super().__init__()

        self._model = model
        self._controller = controller

        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self._ui.currencyBox.addItem('BTC', 'btc')
        self._ui.currencyBox.addItem('ETH', 'eth')

        self._ui.directionBox.addItem('Купить', 'buy')
        self._ui.directionBox.addItem('Продать', 'sell')

        # self._ui.currencyBox.currentIndexChanged[int].connect(self._controller.currency_box_change)
        self._ui.currencyBox.currentIndexChanged.connect(self.currency_box_change)
        # self._ui.directionBox.currentIndexChanged.connect(self._controller.direction_box_change)
        self._ui.directionBox.currentIndexChanged.connect(self.direction_box_change)

        self._ui.giveInput.textChanged.connect(self._controller.give_input_change)
        self._ui.commissionInput.textChanged.connect(self._controller.commission_input_change)
        self._ui.rateInput.textChanged.connect(self._controller.rate_input_change)

        self._ui.refreshButton.clicked.connect(self._controller.refresh_button_clicked)

        self.currency_box.connect(self._controller.currency_box_change)
        self.direction_box.connect(self._controller.direction_box_change)

        self._model.calculate.connect(self.on_calculate)
        self._model.rate.connect(self.on_get_rate)
        self._model.give_cur_label.connect(self.on_give_currency_label)
        self._model.receive_cur_label.connect(self.on_receive_currency_label)

    @Slot(dict)
    def on_calculate(self, value):
        self._ui.netInput.setText('%.8f' % value['net'])
        self._ui.commissionMoneyInput.setText('%.8f' % value['com_money'])
        self._ui.receiveInput.setText('%.8f' % value['receive'])

    @Slot(float)
    def on_get_rate(self, value):
        self._ui.rateInput.setText('%.8f' % value)

    @Slot(int)
    def currency_box_change(self, value):
        data = self._ui.currencyBox.itemData(value)
        self.currency_box.emit(data)

    @Slot(int)
    def direction_box_change(self, value):
        data = self._ui.directionBox.itemData(value)
        self.direction_box.emit(data)

    @Slot(str)
    def on_give_currency_label(self, value):
        self._ui.giveCurLabel.setText(value)

    @Slot(str)
    def on_receive_currency_label(self, value):
        self._ui.receiveCurLabel.setText(value)
