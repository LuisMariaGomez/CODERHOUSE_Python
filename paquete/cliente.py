class Cliente:
    nacionalidad = "Argentina"
    credito = 2000.0

    def __init__(self, nombre:str, dinero_en_cuenta:float):
        self.nombre = nombre
        self.dinero_en_cuenta = dinero_en_cuenta

    def __str__(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print(f"Dinero en cuenta: {self.dinero_en_cuenta}")
        print(f"Credito: {self.credito} $")

    def compar(self, monto:float):
        if monto <= 0:
            print("El monto debe ser mayor a 0.")
            return

        if self.dinero_en_cuenta >= monto:
            self.dinero_en_cuenta -= monto
            print(f"{self.nombre} ha realizado la compra por {monto} $. Su nuevo saldo es {self.dinero_en_cuenta} $")
        elif self.dinero_en_cuenta < monto:
            faltante = monto - self.dinero_en_cuenta
            if faltante > self.credito:
                print(f"{self.nombre} no tiene suficiente dinero. Ni utilizando credito.")
                return
            self.credito -= faltante
            self.dinero_en_cuenta = 0.0
            print(f"{self.nombre} ha realizado la compra por {monto} $ utilizando credito. Su saldo es {self.dinero_en_cuenta} $ y su credito restante es {self.credito} $, en su proxima carga se debiitara el monto utilizado de credito.")

    def cargar_dinero(self, monto_a_cargar:float):
        if monto_a_cargar <= 0:
            print("El monto a cargar debe ser mayor a 0.")
            return

        if self.credito < 2000.0:
            credito_a_recuperar = 2000.0 - self.credito
            if monto_a_cargar >= credito_a_recuperar:
                self.credito = 2000.0
                monto_a_cargar -= credito_a_recuperar
                self.dinero_en_cuenta += monto_a_cargar
                print(f"{self.nombre} ha recuperado todo su credito y le han sobrado {monto_a_cargar} $ que se han cargado a su cuenta. Su nuevo saldo es {self.dinero_en_cuenta} $ y su credito es {self.credito} $.")
            else:
                self.credito += monto_a_cargar
                print(f"{self.nombre} ha recuperado {monto_a_cargar} $ de credito. Su nuevo credito es {self.credito} $.")
        else:
            self.dinero_en_cuenta += monto_a_cargar
            print(f"{self.nombre} ha cargado {monto_a_cargar} $ a su cuenta. Su nuevo saldo es {self.dinero_en_cuenta} $.")
