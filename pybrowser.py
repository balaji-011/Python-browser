import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        nav_bar = QToolBar()
        self.addToolBar(nav_bar)

        back = QAction('Back', self)
        back.triggered.connect(self.browser.back)
        nav_bar.addAction(back)

        forward = QAction('Forward', self)
        forward.triggered.connect(self.browser.forward)
        nav_bar.addAction(forward)

        reload = QAction('Reload', self)
        reload.triggered.connect(self.browser.reload)
        nav_bar.addAction(reload)

        home = QAction('Home', self)
        home.triggered.connect(self.navigate_to_home)
        nav_bar.addAction(home)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        nav_bar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_to_home(self):
        self.browser.setUrl(QUrl('http://bing.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('Python Browser')
window = MainWindow()
app.exec_()
