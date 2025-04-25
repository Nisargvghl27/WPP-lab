class converter:
    methods = {
        "inches": 1,
        "feet": 1 / 12,
        "yards": 1 / 36,
        "miles": 1 / 63360,
        "kilometers": 1 / 39370.1,
        "meters": 1 / 39.3701,
        "centimeters": 1 / 0.393701,
        "millimeters": 1 / 0.0393701,
    }

    def __init__(self, length, unit):
        if unit not in self.methods:
            raise ValueError(f"{unit} is an invalid unit.")
        else:
            self.length_inches = length / self.methods[unit]

    def inches(self):
        return self.length_inches * self.methods["inches"]

    def feet(self):
        return self.length_inches * self.methods["feet"]

    def yards(self):
        return self.length_inches * self.methods["yards"]

    def miles(self):
        return self.length_inches * self.methods["miles"]

    def millimeters(self):  # Fixed spelling
        return self.length_inches * self.methods["millimeters"]

    def centimeters(self):
        return self.length_inches * self.methods["centimeters"]

    def meters(self):
        return self.length_inches * self.methods["meters"]

    def kilometers(self):
        return self.length_inches * self.methods["kilometers"]


abc = float(input("Enter any number which you want to convert: "))

print()
print("Methods: ")
dic = {
    1: "inches",
    2: "feet",
    3: "yards",
    4: "miles",
    5: "kilometers",
    6: "meters",
    7: "centimeters",
    8: "millimeters",
}

for i in dic:
    print(i, "->", dic[i])

print()
n = int(input("Enter the unit you are converting from: "))
m = int(input("Enter the unit you want to convert to: "))
print()

if n in dic and m in dic:
    c = converter(abc, dic[n])
    unit = dic[m]
    method = getattr(c, unit, None)

    if method:
        print(f"Converted value in {unit}: {method()}")
    else:
        print("Invalid conversion!")
else:
    print("Invalid choice!")