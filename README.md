# WeatherForcast
## Overview
The Weather Forecast App is a simple web application that allows users to get current weather 
information for a specified city, state, and country. It utilizes the OpenWeatherMap API to fetch 
weather data and display it to the user.
## Features
- Input form for users to enter the city, state, and country information.
- Display of current weather information, including temperature, weather description, and air quality 
index.
- Responsive design for a user-friendly experience on different devices.
## Technologies Used
- Python
- Flask (Web framework)
- HTML
- CSS (Bootstrap for styling)
- JavaScript (Bootstrap for responsive components)
- OpenWeatherMap API
## How to Run
1. Clone the repository to your local machine.
2. Install the required Python packages using `pip install -r requirements.txt`.
3. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api) and replace the 
placeholder API key in the `main.py` file.
4. Run the application using `python app.py`.
5. Access the application in your web browser at `http://localhost:5000`.
## Usage
1. Enter the desired city, state (optional), and country (optional) in the input form.
2. Click the "Find" button to retrieve and display the current weather information.
3. The application will show the main weather condition, description, an icon representing the 
weather, temperature in Celsius, and air quality index.
## Acknowledgments
- The application uses the [OpenWeatherMap API](https://openweathermap.org/) to fetch weather 
data.
