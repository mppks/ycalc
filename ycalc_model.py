from PySide2.QtCore import QObject, Signal
import yobit_api
from abc import ABC, abstractmethod


class YCalcModel(QObject):
    calculate = Signal(dict)
    rate = Signal(float)
    give_cur_label = Signal(str)
    receive_cur_label = Signal(str)

    @property
    def give_input(self):
        return self._give_input

    @give_input.setter
    def give_input(self, value):
        self._give_input = value
        self.calculation()

    @property
    def commission_input(self):
        return self._commission_input

    @commission_input.setter
    def commission_input(self, value):
        self._commission_input = value
        self.calculation()

    @property
    def rate_input(self):
        return self._rate_input

    @rate_input.setter
    def rate_input(self, value):
        self._rate_input = value
        self.calculation()

    @property
    def currency_box(self):
        return self._currency_box

    @currency_box.setter
    def currency_box(self, value):
        self._currency_box = value
        self.calculation()

    # def give_currency_label(self, value):
    #     self.give_cur_label.emit(value)
    #
    # def receive_currency_label(self, value):
    #     self.receive_cur_label.emit(value)

    @property
    def direction_box(self):
        return self._direction_box

    @direction_box.setter
    def direction_box(self, value):
        self._direction_box = value
        self.calculation()

    def calculation(self):
        """Вызов метода рассчета в зависимости от направления обмена"""
        getattr(self, self.direction_box)()

    def buy(self):
        """Рассчет покупки крипты"""
        inst = Buy(self.give_input, self.commission_input, self.rate_input, self.currency_box)
        # print(inst.calculation())
        self.calculate.emit(inst.calculation())
        self.give_cur_label.emit(inst.give_currency())
        self.receive_cur_label.emit(inst.receive_currency())

    def sell(self):
        """Рассчет продажи крипты"""
        inst = Sell(self.give_input, self.commission_input, self.rate_input, self.currency_box)
        # print(inst.calculation())
        self.calculate.emit(inst.calculation())
        self.give_cur_label.emit(inst.give_currency())
        self.receive_cur_label.emit(inst.receive_currency())

    def get_rate(self):
        """Получение курса"""
        pair = self.currency_box.lower() + "_usd"
        response = yobit_api.PublicApi().get_pair_ticker(pair=pair)
        # TODO: Обработка исключения при отсутствии соединения
        direction = "buy" if self.direction_box == "sell" else "sell"
        value = response[direction] if response else 0
        self.rate.emit(value)

    def __init__(self):
        super().__init__()

        self._give_input = 0
        self._commission_input = 0.2
        self._rate_input = 0
        self._currency_box = 'btc'
        self._direction_box = 'buy'


class Operation(ABC):
    CUR = "usd"

    def __init__(self, give, commission, rate, currency):
        self.give = give
        self.commission = commission
        self.rate = rate
        self.currency = currency

    @abstractmethod
    def calculation(self):
        pass

    @abstractmethod
    def give_currency(self):
        pass

    @abstractmethod
    def receive_currency(self):
        pass


class Buy(Operation):
    def calculation(self):
        value = dict()
        value['com_money'] = self.give/100.2 * self.commission
        value['net'] = self.give - value['com_money']
        if not self.rate:
            value['receive'] = 0
        else:
            value['receive'] = value['net'] / self.rate

        return value

    def give_currency(self):
        return self.CUR

    def receive_currency(self):
        return self.currency


class Sell(Operation):
    def calculation(self):
        value = dict()
        value['net'] = self.give * self.rate
        value['com_money'] = value['net']/100 * self.commission
        value['receive'] = value['net'] - value['com_money']

        return value

    def give_currency(self):
        return self.currency

    def receive_currency(self):
        return self.CUR
