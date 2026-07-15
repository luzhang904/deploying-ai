import requests


def get_weather(city):

    cities = {
        "toronto": (43.6532,-79.3832),
        "new york": (40.7128,-74.0060),
        "london": (51.5072,-0.1276)
    }


    if city.lower() not in cities:
        return "I don't know that city."


    lat,lon = cities[city.lower()]


    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        "&current_weather=true"
    )


    response=requests.get(url)

    data=response.json()


    temp=data["current_weather"]["temperature"]


    return (
        f"The weather in {city.title()} "
        f"is currently around {temp}°C."
    )