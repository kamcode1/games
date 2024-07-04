import requests

def get_weather(api_key, location):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        location_name = data['location']['name']
        region = data['location']['region']
        country = data['location']['country']
        temperature = data['current']['temp_c']
        condition = data['current']['condition']['text']

        print(f"Location: {location_name},{region},{country}")
        print(f"Temprature: {temperature}C")
        print(f"condtion: {condition}")
    else:
        print(f"Failed to get weather data. status code: {response.status_code}")

if __name__ == "__main__":
    api_key = 'a7b0838be24c4b81a5f101133240407'
    location = input("Enter the location: ")

    get_weather(api_key, location)