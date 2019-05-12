from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.command = QtWidgets.QPushButton(self.centralwidget)
        self.command.setGeometry(QtCore.QRect(250, 533, 100, 40))
        self.command.setObjectName("command")
        self.command.setToolTip("Runs the command")

        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(450, 533, 100, 40))
        self.exit.setObjectName("Exit")
        self.exit.setToolTip("Close the App")

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(23, 30, 750, 480))
        self.plainTextEdit.setObjectName("plainTextEdit")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.command.clicked.connect(self.plainTextEdit.clear)
        self.command.clicked.connect(self.run_command)
        self.exit.clicked.connect(sys.exit)

    def run_command(self):
        cmd = "cut -d ' ' -f 3,4,5,6  /proc/cmdline | tee output.txt" #Gets the boot options and writes to a file
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out, err = process.communicate()
        opt = "awk -f options.awk output.txt"
        options = subprocess.Popen(opt, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        opts, err = options.communicate()
        self.plainTextEdit.insertPlainText(str(opts, "utf-8"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Boot Options"))
        self.command.setText(_translate("MainWindow", "Boot Options"))
        self.exit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())