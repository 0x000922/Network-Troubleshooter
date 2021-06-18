import sys
import os
import subprocess
import graphviz_gen

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QPlainTextEdit, QVBoxLayout
from PySide6.QtCore import QFile, QThread, Slot, Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtSvgWidgets import QSvgWidget


class Base(QWidget):
    def __init__(self):
        super(Base, self).__init__()
        self.load_ui()
        # self.thread = Worker()
        self.domain_in = self.ui.findChild(QLineEdit, "domain_in")
        self.text_box = self.ui.findChild(QPlainTextEdit, "log_out")
        self.btn = self.ui.findChild(QPushButton, 'rs_button')
        self.graph_btn = self.ui.findChild(QPushButton, 'graph_btn')

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()


class GraphWindow(QWidget):
    def __init__(self, path):
        super().__init__()
        layout = QVBoxLayout()
        self.svg_wid = QSvgWidget(self)
        self.svg_wid.load(path)
#        self.svg_wid.show()
        layout.addWidget(self.svg_wid)
        self.setLayout(layout)


class Implement(Base):
    def __init__(self):
        super().__init__()
        self.w = None
        print(self.text_box)
        self.btn.clicked.connect(self.run_script)
        self.graph_btn.clicked.connect(self.graph_disp)

    @Slot()
    def run_script(self):
        text_value = self.domain_in.text()
        print(type(text_value))
        out_file = open("output", 'w')
        script_path = "{insert your path here for the bash script }"
        rc = subprocess.run(
            [script_path, text_value],
            stdout=out_file,
            stderr=subprocess.PIPE
        )
        out_file.close()
        self.show_output_box()

    @Slot()
    def show_output_box(self):
        out_file = open("output").read()
        print(out_file)
        self.text_box.clear()
        self.text_box.insertPlainText(out_file)

    def graph_disp(self):
        graphviz_gen.gengraph(self.domain_in.text())
#        if self.w is None:
        print(self.domain_in.text())
        self.w = GraphWindow("final_graph"+self.domain_in.text()+".svg")
        self.w.show()


if __name__ == "__main__":
    app = QApplication([])
    widget = Implement()
    widget.show()
#    widget.show_ui_object()
    sys.exit(app.exec_())
