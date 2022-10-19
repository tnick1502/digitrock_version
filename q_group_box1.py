import os
import subprocess
import sys
from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QComboBox, QPushButton, QMessageBox
from PyQt5.QtCore import Qt


class QVersionBox(QGroupBox):  # Окно и виджеты на нем
    __versions_dir = r'Z:\Digitrock'

    __bat_path = r'./DigitRockUpdateAndRun.bat'

    def __init__(self):
        super().__init__()

        self.setTitle('Выбор версии')
        self.setFixedHeight(72)
        # self.setFixedWidth(350)

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.combo = QComboBox()
        self.btn = QPushButton('Запуск')

        self.combo.setFixedHeight(22)
        self.btn.setFixedHeight(22)

        self.btn.clicked.connect(self.on_btn_click)

        self.layout.addWidget(self.combo)
        self.layout.addWidget(self.btn)

        self.fill_versions()

    def fill_versions(self):
        if not os.path.exists(self.__versions_dir):
            return

        dirs = next(os.walk(self.__versions_dir))[1]

        if not dirs:
            return

        versions = []
        for version in dirs:
            if '.' in version and version != '.idea' and version != '.git':
                versions.append(version)
                continue

        versions.reverse()

        self.combo.addItems(versions)

    def on_btn_click(self):
        with open(self.__bat_path, 'r+') as file:
            bat_file_lines = file.readlines()
            bat_file_lines[0] = f'set version={self.combo.currentText()}\n'
            file.seek(0)
            file.writelines(bat_file_lines)

        pipe = subprocess.Popen(f"{os.path.join(os.getcwd(), self.__bat_path)}",
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        output, error = pipe.communicate()
        if pipe.returncode != 0:
            print(output)
            print(error)

