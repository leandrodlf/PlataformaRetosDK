class ESBSimple:
    def log_operation(self, servicio, accion, datos):
        print(f"🔗 ESB - {servicio} ejecutó: {accion}")
        print(f"   Datos: {datos}")