class Aircraft:
    def __init__(self, flight, aircraft_type, origin, destination,
                 altitude, speed, engine_temp, fuel,
                 oil_pressure, outside_temp, cabin_pressure,
                 engine_rpm, status):
        self.flight = flight
        self.aircraft_type = aircraft_type
        self.origin = origin
        self.destination = destination
        self.altitude = altitude
        self.speed = speed
        self.engine_temp = engine_temp
        self.fuel = fuel
        self.oil_pressure = oil_pressure
        self.outside_temp = outside_temp
        self.cabin_pressure = cabin_pressure
        self.engine_rpm = engine_rpm
        self.status = status


#class Aircraft:
#    def __init__(self, flight):
#        self.fligtht = flight