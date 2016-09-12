from unit import Unit

"""
Units are grouped by category. Units can only be converted to other units of the
same category.

Base units:
temperature: fahrenheit
energy:      joule
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
    "joules": Unit(
        "Joules",
        "energy",
        lambda energy: energy,
        lambda energy: energy,
    ),
    "calories": Unit(
        "Calories",
        "energy",
        lambda energy: energy * 4.1868,
        lambda energy: energy / 4.1868,
    ),
    "kilocalories": Unit(
        "Kilocalories",
        "energy",
        lambda energy: energy * 4186.8,
        lambda energy: energy / 4186.8,
    ),
    "watt hours": Unit(
        "Watt hours",
        "energy",
        lambda energy: energy * 3600,
        lambda energy: energy / 3600,
    )
}
