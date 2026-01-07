# temp_conversion_tool.py
# File location: alx_be_python/fns_and_dsa/temp_conversion_tool.py

# Global conversion factors (defined exactly as the checker expects)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit temperature to Celsius using the global factor.
    """
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius


def convert_to_fahrenheit(celsius):
    """
    Convert Celsius temperature to Fahrenheit using the global factor.
    """
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit


def main():
    print("Temperature Converter (Celsius ↔ Fahrenheit)")
    print("-" * 45)

    try:
        # Get temperature input
        temp_input = input("Enter the temperature to convert: ").strip()
        temperature = float(temp_input)  # Raises ValueError if not numeric

        # Get unit input
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            result = convert_to_celsius(temperature)
            print(f"{temperature:.1f}°F is {result:.2f}°C")
        elif unit == 'C':
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature:.1f}°C is {result:.1f}°F")
        else:
            print("Invalid unit! Please enter 'C' or 'F'.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()