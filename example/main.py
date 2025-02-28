# This Python file uses the following encoding: utf-8
import os
# 注册资源以及自定义的QML组件
import resource.example_rc as rc
import sys

from AppInfo import AppInfo
from component.CircularReveal import CircularReveal
from component.FileWatcher import FileWatcher
from component.FpsItem import FpsItem
from helper.SettingsHelper import SettingsHelper
from PySide6.QtCore import QProcess
from PySide6.QtGui import QGuiApplication
from PySide6.QtNetwork import QNetworkProxy
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtQuick import QQuickWindow, QSGRendererInterface

import FluentUI


def main():
    QQuickWindow.setGraphicsApi(QSGRendererInterface.GraphicsApi.OpenGL)
    os.environ["QT_QUICK_CONTROLS_STYLE"] = "Basic"

    QGuiApplication.setOrganizationName("ChaChaL")
    QGuiApplication.setOrganizationDomain("https://blog.chachal.eu.org/")
    QGuiApplication.setApplicationName("FluentUI")

    SettingsHelper().init()

    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    rootContext = engine.rootContext()
    rootContext.setContextProperty("SettingsHelper", SettingsHelper())
    rootContext.setContextProperty("AppInfo", AppInfo())

    FluentUI.init(engine)
    print(engine.importPathList())

    qml_file = "qrc:/example/qml/App.qml"
    engine.load(qml_file)
    if not engine.rootObjects():
        sys.exit(-1)

    exec = app.exec()
    if exec == 931:
        # QGuiApplication.applicationFilePath()需要打包成exe后才能正确的路径重启，不然这个函数获取的路径是python的路径
        args = QGuiApplication.arguments()[1:]
        QProcess.startDetached(QGuiApplication.applicationFilePath(), args)
    return exec


if __name__ == "__main__":
    main()
