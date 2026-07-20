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
        
def analyze_fleet_exercise(fleet):

    pass

 # "Zatím nic nedělej, ale blok existuje: PASS"


#######

def analyze_fleet(fleet):
    low_fuel_count = 0
    overheating_count = 0

    for aircraft in fleet:

        fuel_status, engine_status = generate_aircraft_report(
            aircraft["fuel"],
            aircraft["engine_temp"]
        )

        if fuel_status == "LOW FUEL":
        
            low_fuel_count += 1

        if engine_status == "ENGINE OVERHEAT":
        
            overheating_count += 1
    
    return low_fuel_count, overheating_count


#######



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
analyze_fleet

# "Tento kód spusť jen tehdy, když spouštím main.py přímo:"
if __name__ == "__main__":
    for aircraft in fleet:
        status = generate_aircraft_report(
            aircraft["fuel"],
            aircraft["engine_temp"]
        )
        print(aircraft["flight"], status)


###################
        

def check_sensors(my_aircraft):
    alerts = []

    if my_aircraft["engine_temp"] >= 100:
        alerts.append("WARNING, HIGH TEMPERATURE!")

    if my_aircraft["fuel"] <= 30:
        alerts.append("WARNING, LOW FUEL!")

    print(alerts)
    return alerts

#tento zapis neni dobry, lepsi je for cyklus, protoze pokud by neexistoval napr. prvek 1 ve fleet, pak by mi to cele spadlo pri jejim volani
#check_sensors(fleet[0])
#check_sensors(fleet[1])
#check_sensors(fleet[2])

for aircraft in fleet:
   check_sensors(aircraft)