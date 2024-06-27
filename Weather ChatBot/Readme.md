# Weather Chatbot

Weather Chatbot is a desktop application built using PyQt5 and the Meteosource Weather API to provide current weather information for any specified location. The app features a user-friendly interface where users can input the name of a place and receive the latest weather data, including temperature, humidity, wind speed, and more.

## Features

- User-friendly and attractive UI with PyQt5.
- Fetches current weather data using the Meteosource Weather API.
- Displays important weather information such as temperature, humidity, wind speed, and more.
- Error handling for invalid place names or API request failures.

## Requirements

- Python 3.11.4
- PyQt5
- Requests

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/ABDULLAHAZHERCH/Projects
   cd Weather_ChatBot
   ```

2. Install the required Python packages:
   ```sh
   pip install pyqt5 requests
   ```

## Usage

1. Get your API key from [RapidAPI Meteosource Weather API](https://rapidapi.com/meteosource-meteosource-default/api/ai-weather-by-meteosource/).

2. Update the API key in the `get_weather` method in `weather_chatbot.py`:

   ```python
   headers = {
       "x-rapidapi-key": "your_rapidapi_key_here",
       "x-rapidapi-host": "ai-weather-by-meteosource.p.rapidapi.com"
   }
   ```

3. Run the application:

   ```sh
   python weather_chatbot.py
   ```

4. Enter the name of a place in the input field and click the "Get Current Weather" button to fetch the latest weather information.

## Example

- **Input:** "London"
- **Output:**
  ```
  Summary: Clear sky
  Temperature: 22°C
  Feels Like: 21°C
  Humidity: 60%
  Wind: 3 m/s NW
  Cloud Cover: 0%
  Pressure: 1015 hPa
  Visibility: 10 km
  UV Index: 5
  ```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [RapidAPI Meteosource Weather API](https://rapidapi.com/meteosource-meteosource-default/api/ai-weather-by-meteosource/) for providing the weather data.

## Contact

- For any questions or suggestions, feel free to open an issue or contact the project maintainers.
