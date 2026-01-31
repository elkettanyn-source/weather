import sys
import os
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap


class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))


        self.setWindowTitle("Weather App")
        self.setFixedSize(400, 520)

        # ===== Central Widget =====
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        # ===== Top Image =====
        self.top_image = QLabel()
        self.top_image.setAlignment(Qt.AlignCenter)
        self.top_image.setPixmap(
            QPixmap(os.path.join(BASE_DIR, "Sun.png")).scaled(140, 140, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )

        

        # ===== Title =====
        title = QLabel("Weather Forecast")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                font-size: 22px;
                font-weight: bold;
                color: #444;
            }
        """)

        # ===== City Input =====
        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Enter city name")
        self.city_input.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                font-size: 14px;
                border-radius: 8px;
                background-color: #f2f2f2;
                color: #000;
            }
        """)

        # ===== Button =====
        self.btn = QPushButton("Get Weather")
        self.btn.setStyleSheet("""
            QPushButton {
                background-color: #6a0dad;
                color: white;
                font-size: 15px;
                padding: 10px;
                border-radius: 8px;
                color: #000;
            }
            QPushButton:hover {
                background-color: #5a00c4;
            }
        """)
        self.btn.clicked.connect(self.get_weather)

        # ===== Weather Info =====
        self.weather_display = QLabel()
        self.weather_display.setAlignment(Qt.AlignCenter)
        self.weather_display.setWordWrap(True)
        self.weather_display.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #222;
                background-color: #f9f9f9;
                padding: 15px;
                border-radius: 10px;
                border: 1px solid #ccc;
            }
        """)

        # ===== Layout Add =====
        main_layout.addWidget(self.top_image)
        main_layout.addWidget(title)
        main_layout.addWidget(self.city_input)
        main_layout.addWidget(self.btn)
        main_layout.addWidget(self.weather_display)

    def get_weather(self):
        city = self.city_input.text().strip()

        if not city:
            self.weather_display.setText("❗ Please enter a city name.")
            return

        # Mock weather data (Portfolio Demo)
        weather_info = f"""
        <h2 style='color:#6a0dad; font-size:20px;'>{city}</h2>
        <p><b>Temperature:</b> <span style='color:#333;'>22°C</span></p>
        <p><b>Feels like:</b> <span style='color:#333;'>24°C</span></p>
        <p><b>Condition:</b> <span style='color:#333;'>Clear Sky ☀️</span></p>
        <p><b>Humidity:</b> <span style='color:#333;'>65%</span></p>
        <p><b>Wind Speed:</b> <span style='color:#333;'>3.5 m/s</span></p>
        """


        self.weather_display.setText(weather_info)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec())
