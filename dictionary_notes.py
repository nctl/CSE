states = {"CA": "California",
          "NJ": "New Jersey",
          "NY": "New York",
          "WI": "Wisconsin"}

# first part is a key; the colon separates this from the entry

print(states["CA"])
print(states["WI"])

nested_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39500000

    },
    "NJ": {
        "NAME": "New Jersey",
        "POPULATION": 9000000

    },
    "NY": {
        "NAME": "New York",
        "POPULATION": 1950000

    },
    "WI": {
        "NAME": "Wisconsin",
        "POPULATION": 550000

     }
}

print(nested_dictionary["CA"]["POPULATION"])
print(nested_dictionary["NY"]["NAME"])

complex_dictionary = nested_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39500000,
        "CITIES": ["Fresno", "San Francisco", "Los Angeles"]
    },
    "NJ": {
        "NAME": "New Jersey",
        "POPULATION": 9000000,
        "CITIES": []
    },
    "NY": {
        "NAME": "New York",
        "POPULATION": 1950000,
        "CITIES": []
    },
    "WI": {
        "NAME": "Wisconsin",
        "POPULATION": 550000
        "CITIES": []
     }
}