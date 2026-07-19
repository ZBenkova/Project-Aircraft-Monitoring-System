fleet = []

with open("aircraft.csv") as file:
    lines = file.readlines()
    print("Lines:", lines)

for line in lines[1:]:
    print("Line:", line)
    data = line.strip().split(",")
    print("Data:", data)

    aircraft = {
        "flight": data[0],
        "altitude": int(data[1]),
        "speed": int(data[2]),
        "engine_temp": int(data[3]),
        "fuel": int(data[4])
    }
    print("aircraft:", aircraft)

    fleet.append(aircraft)



def generate_aircraft_report(fuel, engine_temp):

    if fuel >= 50:
        fuel_status = "FUEL OK"
    else:
        fuel_status = "LOW FUEL"

    if engine_temp >= 100:
        engine_status = "ENGINE OVERHEAT"
    else:
        engine_status = "ENGINE OK"

    return fuel_status, engine_status

def calculate_fuel_warning(fuel):
        if fuel < 20:
            return "CRITICALLY LOW FUEL, LAND IMMEDIATELY"
        else:
            return "FUEL OK"


for aircraft in fleet:

    status = generate_aircraft_report(
        aircraft["fuel"],
        aircraft["engine_temp"]
    )

    print(aircraft["flight"], status)


assert 2 + 2 == 4
assert generate_aircraft_report(60, 130) == ('FUEL OK', 'ENGINE OVERHEAT')
assert generate_aircraft_report(20, 90) == ('LOW FUEL', 'ENGINE OK')
assert generate_aircraft_report(29,100) == ('LOW FUEL', 'ENGINE OVERHEAT')