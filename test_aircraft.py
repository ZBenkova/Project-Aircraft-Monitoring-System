from main import generate_aircraft_report, calculate_fuel_warning

def test_fuel():
    result = generate_aircraft_report(60, 90)

    assert result == ('FUEL OK', 'ENGINE OK')

    
def test_low_fuel_engine():
    result = generate_aircraft_report(20, 90)

    assert result == ('LOW FUEL', 'ENGINE OK')

    
def test_engine_overheat():
    result = generate_aircraft_report(60, 101)

    assert result == ('FUEL OK', 'ENGINE OVERHEAT')


def test_fuel_ok():
    result = calculate_fuel_warning(20)

    assert result == "FUEL OK"
    
def test_critical_low_fuel():
    result = calculate_fuel_warning(19)

    assert result == "CRITICALLY LOW FUEL, LAND IMMEDIATELY"
    