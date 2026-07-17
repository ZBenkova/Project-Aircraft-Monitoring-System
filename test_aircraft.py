from main import generate_aircraft_report

def test_fuel_ok():
    result = generate_aircraft_report(60, 90)

    assert result == ('FUEL OK', 'ENGINE OK')

    
def test_fuel_ok():
    result = generate_aircraft_report(20, 90)

    assert result == ('LOW FUEL', 'ENGINE OK')

    
def test_fuel_ok():
    result = generate_aircraft_report(60, 101)

    assert result == ('FUEL OK', 'ENGINE OVERHEAT')