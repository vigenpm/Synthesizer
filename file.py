import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel
from PyQt5.QtGui import QPixmap, QIcon
from playsound import playsound


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('file.ui', self)
        self.setWindowIcon(QIcon('logo.png'))
        self.rec = False
        self.melody = []
        self.doo.clicked.connect(self.sound)
        self.re.clicked.connect(self.sound)
        self.mi.clicked.connect(self.sound)
        self.fa.clicked.connect(self.sound)
        self.sol.clicked.connect(self.sound)
        self.la.clicked.connect(self.sound)
        self.si.clicked.connect(self.sound)
        self.record.clicked.connect(self.startRecording)
        self.stop.clicked.connect(self.stopRecording)
        self.play.clicked.connect(self.playRecording)
        self.delet.clicked.connect(self.deleteRecording)
        self.open.clicked.connect(self.openMelody)
        self.save.clicked.connect(self.saveMelody)
        self.mel.textChanged.connect(self.saveRecording)

        self.pixmap = QPixmap('logo4.png')
        self.image = QLabel(self)
        self.image.move(220, 10)
        self.image.resize(61, 50)
        self.image.setPixmap(self.pixmap)

    def saveRecording(self):
        self.melody = list(map(int, list(self.mel.text())))

    def saveMelody(self):
        if self.fn.text() != '':
            text = self.fn.text() + ".txt"
            f2 = open(text, 'w')
            f2.write(''.join(map(str, self.melody)))
            f2.close()

    def openMelody(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать мелодию',
                                            '', "(*.txt)")[0]
        self.fn.setText(fname[fname.rindex('/') + 1:fname.index('.')])
        f = open(fname)
        lines = f.readlines()
        if len(lines) > 0:
            self.melody = list(map(int, list(lines[0])))
        f.close()
        if self.melody != []:
            self.mel.setText(''.join(map(str, self.melody)))
        else:
            self.mel.setText('')

    def playRecording(self):
        for i in self.melody:
            if i == 1:
                playsound('do.mp3')
            if i == 2:
                playsound('re.mp3')
            if i == 3:
                playsound('mi.mp3')
            if i == 4:
                playsound('fa.mp3')
            if i == 5:
                playsound('sol.mp3')
            if i == 6:
                playsound('la.mp3')
            if i == 7:
                playsound('si.mp3')
            if i == 0:
                playsound('pause.mp3')

    def stopRecording(self):
        self.rec = False
        self.tek.setText("Свободная игра")

    def startRecording(self):
        self.rec = True
        self.tek.setText("Запись")

    def deleteRecording(self):
        self.melody = []
        if self.melody != []:
            self.mel.setText(''.join(map(str, self.melody)))
        else:
            self.mel.setText('')

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_1:
            playsound('do.mp3')
            if self.rec:
                self.melody.append(1)
        if event.key() == Qt.Key_2:
            playsound('re.mp3')
            if self.rec:
                self.melody.append(2)
        if event.key() == Qt.Key_3:
            playsound('mi.mp3')
            if self.rec:
                self.melody.append(3)
        if event.key() == Qt.Key_4:
            playsound('fa.mp3')
            if self.rec:
                self.melody.append(4)
        if event.key() == Qt.Key_5:
            playsound('sol.mp3')
            if self.rec:
                self.melody.append(5)
        if event.key() == Qt.Key_6:
            playsound('la.mp3')
            if self.rec:
                self.melody.append(6)
        if event.key() == Qt.Key_7:
            playsound('si.mp3')
            if self.rec:
                self.melody.append(7)
        if event.key() == Qt.Key_0:
            playsound('pause.mp3')
            if self.rec:
                self.melody.append(0)
        if self.melody != []:
            self.mel.setText(''.join(map(str, self.melody)))
        else:
            self.mel.setText('')

    def sound(self):
        if self.sender().text() == '1':
            playsound('do.mp3')
            if self.rec:
                self.melody.append(1)
        if self.sender().text() == '2':
            playsound('re.mp3')
            if self.rec:
                self.melody.append(2)
        if self.sender().text() == '3':
            playsound('mi.mp3')
            if self.rec:
                self.melody.append(3)
        if self.sender().text() == '4':
            playsound('fa.mp3')
            if self.rec:
                self.melody.append(4)
        if self.sender().text() == '5':
            playsound('sol.mp3')
            if self.rec:
                self.melody.append(5)
        if self.sender().text() == '6':
            playsound('la.mp3')
            if self.rec:
                self.melody.append(6)
        if self.sender().text() == '7':
            playsound('si.mp3')
            if self.rec:
                self.melody.append(7)
        if self.melody != []:
            self.mel.setText(''.join(map(str, self.melody)))
        else:
            self.mel.setText('')


app = QApplication(sys.argv)
ex = Widget()
ex.show()
sys.exit(app.exec())
