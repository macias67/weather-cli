from app.services.open_weather_service import get_city_weather


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    city_name = "Guadalajara"
    city = get_city_weather(city_name)

    print(city)
