import sys
import random
import math

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
)
from PySide6.QtGui import QPainter
from PySide6.QtCore import QTimer


class SimCanvas(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedSize(500, 500)

        self.agents = [
            {
                "x": random.uniform(0, 500),
                "y": random.uniform(0, 500),
                "angle": random.uniform(0, math.tau),
            }
            for _ in range(20)
        ]

    def update_simulation(self):
        for agent in self.agents:
            agent["angle"] += random.uniform(-0.3, 0.3)

            agent["x"] += math.cos(agent["angle"]) * 2
            agent["y"] += math.sin(agent["angle"]) * 2

            agent["x"] %= self.width()
            agent["y"] %= self.height()

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.fillRect(self.rect(), "white")

        self.draw_agents(painter)

    def draw_agents(self, painter):
        for agent in self.agents:
            x = int(agent["x"])
            y = int(agent["y"])

            painter.drawEllipse(
                x - 5,
                y - 5,
                10,
                10,
            )


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Artificial Life Simulator")

        # Central widget
        central = QWidget()
        self.setCentralWidget(central)

        # Layout
        layout = QVBoxLayout(central)

        # Simulation canvas
        self.canvas = SimCanvas()

        layout.addWidget(self.canvas)

        # Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(
            self.canvas.update_simulation
        )
        self.timer.start(16)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())