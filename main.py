aircraft1 = {
    "flight": "LH123",
    "altitude": 10500,
    "speed": 850,
    "engine_temp": 91,
    "fuel": 22
}

aircraft2 = {
    "flight": "BA456",
    "altitude": 8700,
    "speed": 650,
    "engine_temp": 101,
    "fuel": 69
}

aircraft3 = {
    "flight" : "LH7811",
    "altitude": 4300,
    "speed": 450,
    "engine_temp": 81,
    "fuel": 90
}

fleet = [aircraft1, aircraft2, aircraft3]



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



for aircraft in fleet:

    status = generate_aircraft_report(
        aircraft["fuel"],
        aircraft["engine_temp"]
    )

    print(status)

assert generate_aircraft_report(60, 130) == ('FUEL OK', 'ENGINE OVERHEAT')
assert generate_aircraft_report(20, 90) == ('LOW FUEL', 'ENGINE OK')
assert generate_aircraft_report(29,100) == ('LOW FUEL', 'ENGINE OVERHEAT')