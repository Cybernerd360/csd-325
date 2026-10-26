def city_country(city, country, population='', language=''):
    """Return a string of the form 'city, country - population xxx, language'."""
    if language:
        return f"{city}, {country} - population {population}, {language}"
    elif population:
        return f"{city}, {country} - population {population}"
    else:
        return f"{city}, {country}"

# Step 11: Three required calls (2, 3, and 4 arguments)
print(city_country("Paris", "France"))
print(city_country("New York", "USA", 80000))
print(city_country("Tokyo", "Japan", 50000, "Japanese"))