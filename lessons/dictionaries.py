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

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key-valye pair from a dictionary
# by its key.
schools.pop("Duke")

# Test for the existence of a key
if "Duke" in schools:
    print("Found the key 'Duke' in schools")
else:
    print("No key 'Duke' in schools")


# Update / Reassign a key-value pair
schools["UNC"] = 2000
schools["NCSU"] += 200
# print (schools["UNCCC"])
# Example looping over the keys of  dict
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")
print(schools)

