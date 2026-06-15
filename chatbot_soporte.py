print("=== Chatbot de Soporte Técnico ===")

nombre = input("Ingrese su nombre: ")
area = input("Ingrese su área: ")

print("\nSeleccione una categoría:")
print("1 - Acceso")
print("2 - Red")
print("3 - Software")
print("4 - Hardware")

categoria = input("Opción: ")

while categoria not in ["1", "2", "3", "4"]:
    print("Opción inválida.")
    categoria = input("Ingrese una opción válida: ")

descripcion = input("Describa el problema: ")

print("\nConsultando base de datos...")

if categoria == "1":
    print("\nSolución encontrada:")
    print("Restablezca su contraseña desde el portal de usuarios.")
else:
    print("\nNo se encontró una solución automática.")
    print("Generando ticket...")

print("\n=== Ticket Generado ===")
print("Número de Ticket: 1001")
print("Usuario:", nombre)
print("Área:", area)
print("Estado: Abierto")