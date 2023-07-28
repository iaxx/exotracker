from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit
from PyQt5.QtGui import QColor, QPalette, QFont, QIntValidator
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QEasingCurve, QTimer
from PyQt5.QtCore import QPoint
from getpass import getuser
import sys
import os
import json

class UI(QMainWindow):
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.close_button = QPushButton(self)
        self.close_button.setText('X')
        self.close_button.setStyleSheet('background-color: #242424; color: white; border: none;')
        self.close_button.setFixedSize(30, 30)
        self.close_button.move(self.width() - self.close_button.width(), 0)
        self.close_button.clicked.connect(self.close)
        
        self.setWindowTitle("Exotracker")
        self.setGeometry(200, 200, 639, 420)
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor("#171717"))
        self.setPalette(palette)

        self.font = QFont("Tahoma", 18, QFont.Bold)
        self.userLabel = QLabel("Welcome " + getuser(), self)
        self.userLabel.move(250, 20)
        self.userLabel.setFont(self.font)
        self.userLabel.setStyleSheet("color: white")

        self.font.setPointSize(12)
        self.winsInputLabel = QLabel("Total Wins", self)
        self.winsInputLabel.move(100, 60)
        self.winsInputLabel.setFont(self.font)
        self.winsInputLabel.setStyleSheet("color: white")
        self.winsInputLabel.hide()

        self.totalWinsInput = QLineEdit(self)
        self.totalWinsInput.move(100, 160)
        self.totalWinsInput.setValidator(QIntValidator())
        self.totalWinsInput.setFont(self.font)

        self.gamesInputLabel = QLabel("Total Games", self)
        self.gamesInputLabel.move(400, 120)
        self.gamesInputLabel.setFont(self.font)
        self.gamesInputLabel.setStyleSheet("color: white")
        self.gamesInputLabel.hide()

        self.totalGamesInput = QLineEdit(self)
        self.totalGamesInput.move(400, 160)
        self.totalGamesInput.setValidator(QIntValidator())
        self.totalGamesInput.setFont(self.font)

        self.confirmButton = QPushButton("Confirm", self)
        self.confirmButton.move(300, 220)
        self.confirmButton.setFont(self.font)
        self.confirmButton.setStyleSheet("background-color: #242424; color: white")

        self.font.setPointSize(12)
        self.totalWinsLabel = QLabel("Wins: 0", self)
        self.totalWinsLabel.move(200, 70)
        self.totalWinsLabel.setFont(self.font)
        self.totalWinsLabel.setStyleSheet("color: white")
        self.totalWinsLabel.hide()

        self.totalLossesLabel = QLabel("Losses: 0", self)
        self.totalLossesLabel.move(200, 120)
        self.totalLossesLabel.setFont(self.font)
        self.totalLossesLabel.setStyleSheet("color: white")
        self.totalLossesLabel.hide()

        self.totalGamesLabel = QLabel("Games: 0", self)
        self.totalGamesLabel.move(200, 170)
        self.totalGamesLabel.setFont(self.font)
        self.totalGamesLabel.setStyleSheet("color: white")
        self.totalGamesLabel.hide()

        self.winRateLabel = QLabel("Win Rate: 0%", self)
        self.winRateLabel.move(200, 220)
        self.winRateLabel.setFont(self.font)
        self.winRateLabel.setStyleSheet("color: white")
        self.winsInputLabel.setAlignment(Qt.AlignCenter)
        self.winsInputLabel.setMinimumWidth(200)
        self.gamesInputLabel.setAlignment(Qt.AlignCenter)
        self.gamesInputLabel.setMinimumWidth(200)
        self.totalWinsLabel.setAlignment(Qt.AlignCenter)
        self.totalWinsLabel.setMinimumWidth(200)
        self.totalLossesLabel.setAlignment(Qt.AlignCenter)
        self.totalLossesLabel.setMinimumWidth(200)
        self.totalGamesLabel.setAlignment(Qt.AlignCenter)
        self.totalGamesLabel.setMinimumWidth(200)
        self.winRateLabel.setAlignment(Qt.AlignCenter)
        self.winRateLabel.setMinimumWidth(200)

        self.winRateLabel.hide()

        self.winButton = QPushButton("+1 To Wins", self)
        self.winButton.move(120, 300)
        self.winButton.setFont(self.font)
        self.winButton.setStyleSheet("background-color: #242424; color: white")
        self.winButton.hide()

        self.lossButton = QPushButton("+1 To Losses", self)
        self.lossButton.move(400, 300)
        self.lossButton.setFont(self.font)
        self.lossButton.setStyleSheet("background-color: #242424; color: white")
        self.confirmButton.resize(120, 60)
        self.winButton.resize(120, 60)
        self.lossButton.resize(120, 60)

        self.lossButton.hide()

        self.confirmButton.clicked.connect(self.confirm)
        self.winButton.clicked.connect(self.increment_wins)
        self.lossButton.clicked.connect(self.increment_losses)

    def animate(self, widget, duration, startValue, endValue):
        self.animation = QPropertyAnimation(widget, b"geometry")
        self.animation.setDuration(duration)
        self.animation.setStartValue(startValue)
        self.animation.setEndValue(endValue)
        self.animation.setEasingCurve(QEasingCurve.InOutQuint)
        self.animation.start()

    def welcome_screen(self):
        self.userLabel.setGeometry(250, 20, 0, 30)
        self.totalWinsInput.setGeometry(100, 160, 0, 30)
        self.totalGamesInput.setGeometry(400, 160, 0, 30)
        self.confirmButton.setGeometry(300, 220, 0, 30)

        self.animate(self.userLabel, 250, QRect(0, 20, 0, 30), QRect(250, 20, 1000, 30))
        QTimer.singleShot(500, self.show_wins_input)

    def show_wins_input(self):
        self.winsInputLabel.show()
        self.animate(self.winsInputLabel, 500, QRect(50, 120, 0, 20), QRect(50, 120, 100, 20))
        self.animate(self.totalWinsInput, 500, QRect(50, 160, 0, 30), QRect(50, 160, 200, 30))
        QTimer.singleShot(500, self.show_games_input)

    def show_games_input(self):
        self.gamesInputLabel.show()
        self.animate(self.gamesInputLabel, 500, QRect(400, 120, 0, 20), QRect(400, 120, 130, 20))
        self.animate(self.totalGamesInput, 500, QRect(400, 160, 0, 30), QRect(400, 160, 200, 30))
        QTimer.singleShot(500, self.show_confirm_button)

    def show_confirm_button(self):
        self.animate(self.confirmButton, 300, QRect(278, 220, 0, 45), QRect(278, 220, 100, 45))

    def confirm(self):
        self.userLabel.hide()
        self.totalWinsInput.hide()
        self.totalGamesInput.hide()
        self.confirmButton.hide()
        self.winsInputLabel.hide()
        self.gamesInputLabel.hide()

        self.totalWins = int(self.totalWinsInput.text())
        self.totalGames = int(self.totalGamesInput.text())
        self.totalLosses = self.totalGames - self.totalWins
        self.update_labels()

        self.totalWinsLabel.show()
        self.totalLossesLabel.show()
        self.totalGamesLabel.show()
        self.winRateLabel.show()
        self.winButton.show()
        self.lossButton.show()

        self.data = {"totalWins": self.totalWins, "totalGames": self.totalGames}
        # Create the directory path
        directory = os.path.join(os.environ['LOCALAPPDATA'], 'Exotracker')
        # Create the directory if it doesn't exist
        os.makedirs(directory, exist_ok=True)
        # Create the path for the JSON file
        file_path = os.path.join(directory, 'data.json')
        # Write the JSON file
        with open(file_path, 'w') as outfile:
            json.dump(self.data, outfile)
        outfile.close()  # Close the file after writing

    def increment_wins(self):
        self.totalWins += 1
        self.totalGames += 1
        self.update_labels()
        self.update_data()

    def increment_losses(self):
        self.totalLosses += 1
        self.totalGames += 1
        self.update_labels()
        self.update_data()  

    def update_labels(self):
        self.totalWinsLabel.setText("Wins: " + str(self.totalWins))
        self.totalLossesLabel.setText("Losses: " + str(self.totalLosses))
        self.totalGamesLabel.setText("Games: " + str(self.totalGames))
        self.winRateLabel.setText("WR: " + str(round((self.totalWins / self.totalGames) * 100, 2)) + "%")

    def update_data(self):
        # Update the data
        self.data = {"totalWins": self.totalWins, "totalGames": self.totalGames}
        # Create the path for the JSON file
        file_path = os.path.join(os.environ['LOCALAPPDATA'], 'Exotracker', 'data.json')
        # Write the JSON file
        with open(file_path, 'w') as outfile:
            json.dump(self.data, outfile)


if __name__ == "__main__":
    App = QApplication(sys.argv)

    window = UI()
    window.show()

    # Create the path for the JSON file
    file_path = os.path.join(os.environ['LOCALAPPDATA'], 'Exotracker', 'data.json')
    # Check if the JSON file exists
    if os.path.isfile(file_path):
        with open(file_path) as json_file:
            data = json.load(json_file)
            window.totalWinsInput.setText(str(data["totalWins"]))
            window.totalGamesInput.setText(str(data["totalGames"]))
            window.confirm()
    else:
        window.welcome_screen()

    sys.exit(App.exec())
