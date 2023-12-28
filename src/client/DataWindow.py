from PySide6.QtWidgets import QDialog, QLineEdit, QComboBox, QDateEdit
from PySide6.QtCore import QDate
from src.client.ui_data import Ui_Dialog

TableFields = {
    "Users": [
        [QLineEdit, "login", 0],
        [QLineEdit, "password", 0],
        [QComboBox, ["Admin", "Client"], 0]
    ],
    "Applications": [
        [QLineEdit, "Application_number", 0],
        [QLineEdit, "Date_added", 0],
        [QLineEdit, "Fault_type", 0],
        [QLineEdit, "Description_problem", 0],
        [QLineEdit, "id_cars", 0],
        [QLineEdit, "id_client", 0],
        [QLineEdit, "id_application_status", 0],
    ],
    "Cars": [
        [QLineEdit, "brand", 0],
        [QLineEdit, "Model", 0],
    ],
    "Client": [
        [QLineEdit, "name", 0],
        [QLineEdit, "fio", 0],
        [QLineEdit, "phone", 0],
        [QLineEdit, "Email", 0],
    ],
    "Application_statuses": [
        [QLineEdit, "titles_applications", 0],
    ],
}


class DataWindow(QDialog):
    def __init__(self, access, table):
        super(DataWindow, self).__init__()
        self.access = access
        self.table = table
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.back.clicked.connect(lambda: self.close())
        self.createFields()
        self.show()

    def createFields(self):
        current_table = TableFields[self.table]
        for item in current_table:
            widget = item[0]()
            match widget:
                case QLineEdit():
                    widget.setPlaceholderText(item[1])
                case QComboBox():
                    widget.addItems(item[1])
                case QDateEdit():
                    widget.setCalendarPopup(True)
                case _:
                    print("Виджет неизвестного типа")
                    return
            if self.access != item[2]:
                widget.setEnabled(False)
            widget.setMinimumHeight(45)
            a: QDateEdit
            self.ui.DataContainer.addWidget(widget)

    def GetData(self) -> list:
        # TODO проверка на отсутствие данных
        values: list = ['0']
        for layout_item in layout_widgets(self.ui.DataContainer):
            widget = layout_item.widget()
            values.append(get_data_from_widget(widget))
        return values

    def SetData(self, q_table):
        data: list = []
        index = q_table.selectedIndexes()
        for i in range(1, len(index)):
            data.append(q_table.model().data(index[i]))

        widgets: list = []
        for layout_item in layout_widgets(self.ui.DataContainer):
            widget = layout_item.widget()
            widgets.append(widget)
        for i in range(len(data)):
            set_data_for_widget(widgets[i], data[i])

def layout_widgets(layout):
    return (layout.itemAt(i) for i in range(layout.count()))

def set_data_for_widget(widget, data):
    match widget:
        case QLineEdit(): widget.setText(data)
        case QComboBox(): widget.setCurrentIndex(int(data))
        case QDateEdit(): widget.setDate(QDate.fromString(data))
        case _: print("Виджет неизвестного типа")

def get_data_from_widget(widget):
    match widget:
        case QLineEdit(): return widget.text()
        case QComboBox(): return widget.currentIndex()
        case QDateEdit(): return widget.text()
        case _: print("Виджет неизвестного типа")
