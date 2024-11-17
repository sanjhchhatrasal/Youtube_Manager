file = open("txt.py", "w")

try:
    file.write("Sanjh Chhatrasal")
finally:
    file.close()


with open("txt.py", "w") as file:
    file.write("Sanjh")