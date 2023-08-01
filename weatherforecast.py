import requests

def get_weather(api_key, location, option):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if data.get("cod") == 200:
            if option == 1:
                temperature = data["main"]["temp"]
                print(f"Temperature: {temperature}°C")
            elif option == 2:
                wind_speed = data["wind"]["speed"]
                print(f"Wind Speed: {wind_speed} m/s")
            elif option == 3:
                atmospheric_pressure = data["main"]["pressure"]
                print(f"Atmospheric Pressure: {atmospheric_pressure} hPa")
            else:
                print("Invalid option.")
        else:
            print("Error: Unable to fetch weather data.")

    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    api_key = "9d95c564881b357571cd38255370b54c"  # Replace with your actual API key from OpenWeatherMap

    while True:
        print("Options:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        option = int(input("Enter your choice: "))

        if option == 0:
            print("Exiting the program.")
            break
        elif option >= 1 and option <= 3:
            location = input("Enter the location (city name, country): ")
            get_weather(api_key, location, option)
        else:
            print("Invalid option. Please try again.")
