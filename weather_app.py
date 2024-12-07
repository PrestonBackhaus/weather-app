import requests
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPENWEATHERMAP_API_KEY")

favorite_cities = []

# Get the weather data from OpenWeatherMap API
def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    # Check if the response is successful
    if response.status_code == 200:
        weather_data = response.json() # Load JSON data
        if not weather_data: # Check if weather_data is empty
            print("Invalid city name.")
        else:
            display_weather(weather_data)
    else:
        return "Error obtaining data: {response.status_code}"
    
# Display the weather data
def display_weather(data):
    print(f"City: {data["name"]}") # Display city name
    print(f"Description: {data["weather"][0]["main"]}, {data["weather"][0]["description"]}") # Display weather description
    print(f"Current Temperature (in Kelvin): {data["main"]["temp"]} K") # Display temperature data

# Add a city to the favorite list
def add_favorite(city):
    if city in favorite_cities:
        return "City already in favorites."
    elif len(favorite_cities) < 3: # Limit to 3 favorite cities
        favorite_cities.append(city)
        return "City added to favorites."
    else:
        return "You can only have 3 favorite cities."
    
# Remove a city from the favorite list
def remove_favorite(city):
    if city in favorite_cities:
        favorite_cities.remove(city)
        return "City removed from favorites."
    else:
        return "City not found in favorites."
    
# Display weather for favorite cities
def display_favorites():
    print("Displaying all favorite cities weather data...")
    for city in favorite_cities:
        get_weather(city)
        print("\n")

# Main function
def main():
    while True:
        print("1. Get weather for a city")
        print("2. Add a city to favorites")
        print("3. Remove a city from favorites")
        print("4. Display favorite cities")
        print("5. Exit")
        choice = input("Make a selection: ")
        print("\n")
        if choice == "1": # Get weather for a city
            city = input("Enter city name: ")
            get_weather(city)
        elif choice == "2": # Add a city to favorites
            print("Current favorite cities: ", favorite_cities)
            city = input("Enter city to be added: ")
            print(add_favorite(city))
        elif choice == "3": # Remove a city from favorites
            print("Current favorite cities: ", favorite_cities)
            city = input("Enter city to be removed: ")
            print(remove_favorite(city))
        elif choice == "4": # Display favorite cities weather data
            display_favorites()
        elif choice == "5": # End program
            break
        else:
            print("Please enter a valid selection.")
        print("\n")

if __name__ == "__main__":
    main()