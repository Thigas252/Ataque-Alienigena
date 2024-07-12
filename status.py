class StatusJogo():
    def __init__(self, opc):
        self.opc = opc
    
    def resetStatus(self):
        self.naves_restantes = self.opc.nave_vidas
        self.pontos = 0