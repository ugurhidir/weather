# Simple Weather App (Command-Line)

A command-line Python application that fetches and displays current weather information for a given city using the OpenWeatherMap API.

## Features

-   Prompts the user to enter a city name.
-   Uses the OpenWeatherMap API to retrieve current weather data for the specified city.
-   Displays key weather information, including:
    -   Condition (e.g., Clear, Clouds, Rain)
    -   Temperature (in Celsius)
    -   Feels Like Temperature (in Celsius)
    -   Humidity (%)
    -   Wind Speed (m/s)
    -   Visibility (km)
-   Handles various error conditions, such as:
    -   Invalid API key
    -   City not found
    -   Network connection issues
    -   Invalid responses from the API
-   Provides a user-friendly command-line interface.

## Technologies Used

-   Python 3
-   `requests` library (for making HTTP requests to the API)
-   `json` module (for parsing JSON data)
-   String formatting (f-strings)
-   Error handling with `try-except` blocks
-   Basic command-line user interaction

## How to Run

1.  Sign up for a free account at [https://openweathermap.org/](https://openweathermap.org/) and obtain an API key.
2.  Clone this repository or download the Python file (e.g., `hava_durumu.py`).
    ```bash
    
    git clone https://github.com/ugurhidir/weather.git
    cd weather
    ```
    (If you download the file directly, navigate to its directory.)
3.  Install the `requests` library:
    ```bash
    pip install requests
    ```
4.  Open the Python file in a text editor and replace `"YOUR_OPENWEATHERMAP_API_KEY"` with your actual API key.
5.  Run the application using the following command in your terminal:
    ```bash
    python hava_durumu.py
    ```
    (Replace `hava_durumu.py` with your actual Python file name if it's different.)

## How to Use

1.  Run the script as described above.
2.  Enter the name of the city you wish to get weather information for when prompted.
3.  The application will display the current weather conditions for that city.
4.  To exit the application, enter 'q' when prompted for a city name.

## API Key Security

**Important:** Never commit your API key directly to a public repository. If you plan to share your code, consider using environment variables or a configuration file to store your API key securely.