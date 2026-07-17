#pokud je teplota > 90 → HIGH TEMPERATURE
#pokud je tlak oleje < 30 → LOW OIL PRESSURE
#pokud je palivo < 20 → LOW FUEL

def check_sensor(sensor):
    alerts = []

    if sensor["temperature"] > 90:
        alerts.append("HIGH TEMPERATURE")
    
    if sensor["oil_pressure"] < 30:
        alerts.append("LOW OIL PRESSURE")

    return alerts
