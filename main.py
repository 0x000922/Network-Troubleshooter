# This Python file uses the following encoding: utf-8
import sys
import os
import subprocess

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PySide6.QtCore import QFile, Slot
from PySide6.QtUiTools import QUiLoader


class Base(QWidget):
    def __init__(self):
        super(Base, self).__init__()
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()


class Implement(Base):
    def __init__(self):
        super().__init__()
        self.domain_in = self.ui.findChild(QLineEdit, "domain_in")

        btn = self.ui.findChild(QPushButton, 'rs_button')
        btn.clicked.connect(self.run_script)

    def show_ui_object(self):
        print(self.ui)

    def run_script(self):
        text_value = self.domain_in.text()
        print(type(text_value))
        out_file = open("output",'')
        script_path = "/home/creater3494/Projects/Major project/tracescripts/trace.sh"
        rc = subprocess.run(
            [script_path, text_value],
            capture_output=True,
            stdout= out_file
        )
        print(rc)
        print(rc.stdout.decode("utf-8"))
#        print("script test")

    def use_run_script(self):
        pass

    def show_output_box(self):
        pass

    def read_script_output(self):
        pass


if __name__ == "__main__":
    app = QApplication([])
    widget = Implement()
    widget.show()
    widget.show_ui_object()
    sys.exit(app.exec_())
