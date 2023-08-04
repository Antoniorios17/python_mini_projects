def miles_to_mk(miles):
    km = miles * 1.6
    result = f"{miles} miles are {km:.1f} mk"
    return result

print(miles_to_mk(50))
print(miles_to_mk(400))
print(miles_to_mk(1))
