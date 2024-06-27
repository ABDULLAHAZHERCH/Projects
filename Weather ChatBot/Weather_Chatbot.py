import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Weather Chatbot')
        self.setGeometry(100, 100, 500, 500)
        
        layout = QVBoxLayout()

        self.placeLabel = QLabel('Enter a place name:')
        self.placeLabel.setFont(QFont('Arial', 14))
        layout.addWidget(self.placeLabel)

        self.placeInput = QLineEdit(self)
        self.placeInput.setFont(QFont('Arial', 14))
        layout.addWidget(self.placeInput)

        self.searchButton = QPushButton('Get Current Weather', self)
        self.searchButton.setFont(QFont('Arial', 14))
        self.searchButton.setStyleSheet('background-color: #000000; color: white;')
        self.searchButton.clicked.connect(self.get_weather)
        layout.addWidget(self.searchButton)

        self.resultArea = QTextEdit(self)
        self.resultArea.setFont(QFont('Arial', 12))
        self.resultArea.setReadOnly(True)
        layout.addWidget(self.resultArea)

        self.setLayout(layout)
    
    def get_weather(self):
        place_name = self.placeInput.text()
        if place_name:
            try:
                # Finding place coordinates
                url = "https://ai-weather-by-meteosource.p.rapidapi.com/find_places"
                querystring = {"text": place_name, "language": "en"}
                headers = {
                    "x-rapidapi-key": "your_rapidapi_key_here",
                    "x-rapidapi-host": "ai-weather-by-meteosource.p.rapidapi.com"
                }
                response = requests.get(url, headers=headers, params=querystring)
                data = response.json()

                if data:
                    lat = data[0]['lat']
                    lon = data[0]['lon']
                    timezone = data[0]['timezone']

                    # Getting weather information
                    url = "https://ai-weather-by-meteosource.p.rapidapi.com/current"
                    querystring = {"lat": lat, "lon": lon, "timezone": timezone, "language": "en", "units": "metric"}
                    response = requests.get(url, headers=headers, params=querystring)
                    weather_data = response.json()

                    # Extracting and formatting weather information
                    current = weather_data['current']
                    weather_info = (
                        f"Summary: {current['summary']}\n"
                        f"Temperature: {current['temperature']}°C\n"
                        f"Feels Like: {current['feels_like']}°C\n"
                        f"Humidity: {current['humidity']}%\n"
                        f"Wind: {current['wind']['speed']} m/s {current['wind']['dir']}\n"
                        f"Cloud Cover: {current['cloud_cover']}%\n"
                        f"Pressure: {current['pressure']} hPa\n"
                        f"Visibility: {current['visibility']} km\n"
                        f"UV Index: {current['uv_index']}\n"
                    )

                    self.resultArea.setText(weather_info)
                else:
                    self.resultArea.setText("Place not found.")
            except Exception as e:
                self.resultArea.setText(f"Error: {str(e)}")
        else:
            self.resultArea.setText("Please enter a place name.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WeatherApp()
    ex.show()
    sys.exit(app.exec_())
