fleet = []

with open("aircraft.csv") as file:
    lines = file.readlines()
    print("Lines:", lines)

for line in lines[1:]:
    print(f"Line: {line}") #nebo: print("Line:", line)
    
    data = line.strip().split(",")

    aircraft = {
        "flight": data[0],
        "aircraft_type": data[1],
        "origin": data[2],
        "destination": data[3],
        "altitude": int(data[4]),
        "speed": int(data[5]),
        "engine_temp": int(data[6]),
        "fuel": int(data[7]),
        "oil_pressure": int(data[8]),
        "outside_temp": int(data[9]),
        "cabin_pressure": int(data[10]),
        "engine_rpm": int(data[11]),
        "status": data[12]

    }

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

    return alerts

#tento zapis neni dobry, lepsi je for cyklus, protoze pokud by neexistoval napr. prvek 1 ve fleet, pak by mi to cele spadlo pri jejim volani
#check_sensors(fleet[0])
#check_sensors(fleet[1])
#check_sensors(fleet[2])

for aircraft in fleet:
   check_sensors(aircraft)

for aircraft in fleet:
    alerts = check_sensors(aircraft)

    print(f"Flight: {aircraft['flight']}")

    if alerts:
        for alert in alerts:
            print(f"  - {alert}")
    else:
        print("  - No alerts")

    print()

################

for aircraft in fleet:
    def moje_funkce(parametr_palivo):
        alerts = []
        if parametr_palivo < 20:
            alerts.append("LOW FUEL")
        return alerts

moje_funkce(aircraft["fuel"])


######################

def moje_funkce(parametr_palivo):
        alerts = []
        if parametr_palivo < 20:
            alerts.append("LOW FUEL")
        return alerts
for aircraft in fleet:
    moje_funkce(aircraft["fuel"])

