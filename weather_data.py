# Case Study: Weather Data Analysis

# Analyze weather data (temperature, humidity, etc.) for a given region
# Use variables and data types to store weather data
# Implement conditional statements to determine weather conditions
# (sunny, rainy, etc.)
# Use functions to calculate average temperature and humidity, and print results.


def calculate_average(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

def determine_weather_condition(temperature, humidity):
    if temperature > 30 and humidity < 60:
        return "Sunny"
    elif temperature < 20 and humidity > 70:
        return "Rainy"
    else:
        return "Cloudy"


def main():
    temprature = []
    humidity = []
    
    # data values from user
    num_days = int(input("Enter the number of days for which you have weather data: "))
    for _ in range(num_days):
        temp = float(input(f"Enter temperature for day {_ + 1}: "))
        hum = float(input(f"Enter humidity for day {_ + 1}: "))
        temprature.append(temp)
        humidity.append(hum)
    
    # Calculate average temperature and humidity
    avg_temp = calculate_average(temprature)
    avg_humidity = calculate_average(humidity)
    weather_condition = determine_weather_condition(avg_temp, avg_humidity)
    
    # Print the results
    print(f"Average Temperature: {avg_temp:.2f}°C")
    print(f"Average Humidity: {avg_humidity:.2f}%")
    print(f"Weather Condition: {weather_condition}")
    
    
main()