inventario = (
  "mouse":10,
  "teclado":6,
  "monitor":3,
)
producto = input (producto a retirar:)lower()
cantidad = int(input("cantidad: "))

if producto in inventario:
  if cantidad<= inventario[producto]:
    inventario[producto] = cantidad
    print("retiro exitoso. ")
  else:
    print("error: no hay suificientes unidades.")
else:
    print("producto no encontrado.")

print("inventario actualizaado:",inventario)
