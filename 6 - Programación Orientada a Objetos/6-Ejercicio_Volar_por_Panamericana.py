ushuaia=0
buenos_aires=3078
valparaiso=4533
bahia_prudhoe=17958

class Ave:
    def arranca_en(self,ciudad):
        self.ciudad_actual=ciudad
    
    def volar_por_panamericana(self,ciudad_destino):
        kilometros=abs(self.ciudad_actual-ciudad_destino)
        self.volar(kilometros)
        self.ciudad_actual=ciudad_destino