"""Demonstrations of dictionary capabilities."""

# Declaring the type of a dictionary
schools: dict[str, int]


# Initialize to an empty dictionary
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation
print(schools)


# Access a value by its key --look up
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from a dictionary
# by its key
schools.pop("Duke")

# Test fir existence of a key
is_duke_present: bool = "Duke" in schools
print(f" Duke is present: {is_duke_present}")

# or...
if "Duke" in schools:
    print("Found the key 'Duke' in schools")
else:
    print("No key 'Duke' in schools")

# Update / Reassign
schools["UNC"] = 20000
schools["NCSU"] += 200

# Demonstration od dictionary literals

# Empty dictionary literal
schools = {}    # Same as dict()

# Alternatively initialize key-value pairs
schools = {"UNC": 19400, "Duke": 6717, "NCSU": 26150}
print(schools)

# What happens when a key doesnt exist?
# print(schools["UNCC"])

for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")