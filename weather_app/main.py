from weather import get_weather


def main():
    print("===== WEATHER APP =====")
    city=input("Enter the City: ")
    if not city.strip():
        print("Please enter a city name.")
        return
    get_weather(city)
if __name__=="__main__":
    main()