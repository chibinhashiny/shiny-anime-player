import os
import sys
is_on_library = True
is_on_configs = True
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QApplication,
                               QTableWidget,
                               QTableWidgetItem)
from anime_list import anime_array
import anime_list

class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.is_on_library = is_on_library
        self.is_on_configs = is_on_configs

        self.setWindowIcon(QtGui.QIcon("icon.ico"))
        self.setWindowTitle("Shiny Anime Player")

        self.exit_btn = QtWidgets.QPushButton("Sair")
        self.configs_btn = QtWidgets.QPushButton("Configurações")
        self.library_btn = QtWidgets.QPushButton("Biblioteca")
        self.anime_widget_list = QtWidgets.QListWidget()
        self.episodes_list = QtWidgets.QListWidget()
        self.selected_anime = None

        self.layout = QtWidgets.QVBoxLayout(self)

        self.layout.addWidget(self.anime_widget_list,
                              alignment=QtCore.Qt.AlignRight)
        self.layout.addStretch()
        self.anime_widget_list.hide()

        self.layout.addWidget(self.episodes_list,
                              alignment=QtCore.Qt.AlignCenter)

        self.layout.addStretch()
        self.episodes_list.hide()

        self.layout.addWidget(self.exit_btn,
                              alignment=QtCore.Qt.AlignLeft)
        self.layout.addStretch()

        self.layout.addWidget(self.library_btn, alignment=QtCore.Qt.AlignLeft)
        self.layout.addStretch()
        self.library_btn.setFixedSize(150,300)

        self.layout.addWidget(self.configs_btn, alignment=QtCore.Qt.AlignLeft)
        self.configs_btn.setFixedSize(150, 50)

        self.exit_btn.clicked.connect(self.close)

        self.library_btn.clicked.connect(self.library_toggle)

        self.configs_btn.clicked.connect(self.config_toggle)

        self.anime_widget_list.itemClicked.connect(self.library_list_stuff)
        self.episodes_list.itemDoubleClicked.connect(self.play_episodes)



    def library_shi(self):
        self.anime_widget_list.clear()
        for i in anime_array:
            self.anime_widget_list.addItem(i)


    @QtCore.Slot()
    def library_list_stuff(self):
        item = self.anime_widget_list.currentItem()
        self.selected_anime = item.text()
        if item is not None:
            self.episodes_list.clear()
            if item.text() in anime_array:
              episodes = anime_list.scan_shi(option=self.selected_anime)
        for i in episodes:
            self.episodes_list.addItem(i)
            print(episodes)
        self.episodes_list.show()

    @QtCore.Slot()
    def play_episodes(self):
        selected_episode = self.episodes_list.currentItem()
        if selected_episode is not None:
            anime_list.open_video_file(selected_episode.text(), self.selected_anime)


    @QtCore.Slot()
    def close(self):
        sys.exit()

    @QtCore.Slot()
    def config_toggle(self):
        if self.is_on_configs:
            self.is_on_configs = not self.is_on_configs
            self.library_btn.hide()
            self.configs_btn.setText("Voltar")
        else:
            self.is_on_configs = not self.is_on_configs
            self.library_btn.show()
            self.configs_btn.setText("Configurações")
        print(self.is_on_configs)

    @QtCore.Slot()
    def library_toggle(self):
        if self.is_on_library:
           # self.library_list_stuff()
            self.library_shi()
            self.anime_widget_list.show()
            self.is_on_library = not self.is_on_library
            self.configs_btn.hide()
        else:
            self.is_on_library = not self.is_on_library
            self.episodes_list.hide()
            self.anime_widget_list.hide()
            self.configs_btn.show()
        print(self.is_on_library)


