from main import generate_aircraft_report, calculate_fuel_warning

def test_fuel_ok():
    result = generate_aircraft_report(60, 90)

    assert result == ('FUEL OK', 'ENGINE OK')

    
def test_fuel_ok():
    result = generate_aircraft_report(20, 90)

    assert result == ('LOW FUEL', 'ENGINE OK')

    
def test_fuel_ok():
    result = generate_aircraft_report(60, 101)

    assert result == ('FUEL OK', 'ENGINE OVERHEAT')

def test_low_fuel():
    assert calculate_fuel_warning(20) == "LOW FUEL"


#def test_calculate_fuel_warning():
#    assert calculate_fuel_warning(30) == "CRITICALLY LOW FUEL, LAND IMMEDIATELY"
    