from aircraft import Aircraft

fleet = []

# Načtení dat z CSV
with open("aircraft.csv") as file:
    lines = file.readlines()

for line in lines[1:]:
    data = line.strip().split(",")

    aircraft = Aircraft(
        data[0],
        data[1],
        data[2],
        data[3],
        int(data[4]),
        int(data[5]),
        int(data[6]),
        int(data[7]),
        int(data[8]),
        int(data[9]),
        int(data[10]),
        int(data[11]),
        data[12]
    )

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


def analyze_fleet(fleet):
    low_fuel_count = 0
    overheating_count = 0

    for aircraft in fleet:

        fuel_status, engine_status = generate_aircraft_report(
            aircraft.fuel,
            aircraft.engine_temp
        )

        if fuel_status == "LOW FUEL":
            low_fuel_count += 1

        if engine_status == "ENGINE OVERHEAT":
            overheating_count += 1

    return low_fuel_count, overheating_count


def check_sensors(my_aircraft):
    alerts = []

    if my_aircraft.engine_temp >= 100:
        alerts.append("WARNING, HIGH TEMPERATURE!")

    if my_aircraft.fuel <= 30:
        alerts.append("WARNING, LOW FUEL!")

    return alerts


# Výpis reportu pro všechna letadla
for aircraft in fleet:

    status = generate_aircraft_report(
        aircraft.fuel,
        aircraft.engine_temp
    )

    print(aircraft.flight, status)


print("\n=========================")
print("SENSOR ALERTS")
print("=========================\n")

for aircraft in fleet:

    alerts = check_sensors(aircraft)

    print(f"Flight: {aircraft.flight}")

    if alerts:
        for alert in alerts:
            print(f"  - {alert}")
    else:
        print("  - No alerts")

    print()


low_fuel, overheating = analyze_fleet(fleet)

print("=========================")
print("FLEET SUMMARY")
print("=========================")
print(f"Aircraft with low fuel: {low_fuel}")
print(f"Aircraft with engine overheating: {overheating}")


# Jednoduché testy
assert 2 + 2 == 4
assert generate_aircraft_report(60, 130) == ("FUEL OK", "ENGINE OVERHEAT")
assert generate_aircraft_report(20, 90) == ("LOW FUEL", "ENGINE OK")
assert generate_aircraft_report(29, 100) == ("LOW FUEL", "ENGINE OVERHEAT")


if __name__ == "__main__":
    print("\nProgram finished successfully.")