class SensorCalidadAire:
    def __init__(self, humo, benceno, nh3, co2, nox, alcohol):
        self.humo = humo
        self.benceno = benceno
        self.nh3 = nh3
        self.co2 = co2
        self.nox = nox
        self.alcohol = alcohol
        
    # Getter para humo
    def get_humo(self):
        return self.humo

    # Getter para benceno
    def get_benceno(self):
        return self.benceno

    # Getter para nh3
    def get_nh3(self):
        return self.nh3

    # Getter para co2
    def get_co2(self):
        return self.co2

    # Getter para nox
    def get_nox(self):
        return self.nox

    # Getter para alcohol
    def get_alcohol(self):
        return self.alcohol
    
# Creación del objeto
sensor_calidad_aire = SensorCalidadAire(45,26,85,28,95,12)