from unit import Unit

"""
Units are grouped by category. Units can only be converted to other units of the
same category.

Base units:
temperature: fahrenheit
"""

conversions = {
    "celsius": Unit(
        "Celsius",
        "temperature",
        lambda temp: 1.8*temp + 32,
        lambda temp: (temp - 32) / 1.8,
    ),
    "fahrenheit": Unit(
        "Fahrenheit",
        "temperature",
        lambda temp: temp,
        lambda temp: temp,
    ),
    "kelvin": Unit(
        "Kelvin",
        "temperature",
        lambda temp: 1.8*(temp - 273.15) + 32,
        lambda temp: ((temp - 32) / 1.8) + 273.15,
    ),
    "chirps": Unit(
        "Cricket Chirps",
        "temperature",
        lambda temp: temp/4 + 40,
        lambda temp: (temp - 40) * 4,
    ),
}
