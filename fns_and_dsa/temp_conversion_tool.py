FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
def convert_to_celsius(fahrenheit):
    if not isinstance(fahrenheit, (int, float)):
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit
def main():
    try:
        temperature = float(input("Enter the temperature: "))
        scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if scale == 'F':
            converted_temperature = convert_to_celsius(temperature)
            print(f"{temperature} Fahrenheit is {converted_temperature:.2f} Celsius.")
        elif scale == 'C':
            converted_temperature = convert_to_fahrenheit(temperature)
            print(f"{temperature} Celsius is {converted_temperature:.2f} Fahrenheit.")
        else:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as ve:
        print(str(ve))

if __name__ == "__main__":
    main()