aircraft = {
    "flight": "LH123",
    "altitude": 10500,
    "speed": 850,
    "engine_temp": 91,
    "fuel": 22
}

print(f"Flight: {aircraft['flight']}")

def check_fuel(X):
    if X >= 30:
        return "OK"
    else:
        return "LOW FUEL"
    
status = check_fuel(aircraft["fuel"])
print(status)

if status == "LOW FUEL":
    print("Pilot must land immediately!")


def check_engine_temperature(eng_temp):
    if eng_temp >= 100:
        return "ENGINE OVERHEAT"
    else:
        return "ENGINE OK"

status = check_engine_temperature(aircraft["engine_temp"])
print(status)

if status == "ENGINE OVERHEAT":
    print("Pilot must land immediately!")