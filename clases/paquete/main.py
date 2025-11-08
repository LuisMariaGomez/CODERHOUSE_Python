from cliente import Cliente

c1 = Cliente("Luis", 1000.0)

print(c1)                   # Información del cliente
c1.compar(1000.0)           # Prueba de compra con saldo suficiente
c1.compar(1500.0)           # Prueba de compra con saldo insuficiente pero con crédito  
c1.cargar_dinero(1000.0)    # Carga de dinero al cliente, pero que solo recupere parte del crédito
c1.cargar_dinero(2000.0)    # Carga de dinero al cliente que recupera todo el crédito y quede en saldo
c1.compar(8500.0)           # Prueba de compra con saldo y credito insuficiente