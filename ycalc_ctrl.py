from PySide2.QtCore import QObject, Slot


class YCalcController(QObject):
    def __init__(self, model):
        super().__init__()

        self._model = model

    @Slot(str)
    def give_input_change(self, value):
        self._model.give_input = float(value)

    @Slot(str)
    def commission_input_change(self, value):
        self._model.commission_input = float(value)

    @Slot(str)
    def rate_input_change(self, value):
        self._model.rate_input = float(value)

    @Slot(str)
    def currency_box_change(self, value):
        self._model.currency_box = value

    @Slot(int)
    def direction_box_change(self, value):
        self._model.direction_box = value

    @Slot(bool)
    def refresh_button_clicked(self):
        self._model.get_rate()
