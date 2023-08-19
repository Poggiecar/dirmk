import os
carpeta_principal = input("Nombre de la maquina: ")

# Crear la carpeta principal
os.makedirs(carpeta_principal)

# Crear las subcarpetas
subcarpeta1 = os.path.join(carpeta_principal, 'Nmap')
subcarpeta2 = os.path.join(carpeta_principal, 'Vulnerabilidades')
subcarpeta3 = os.path.join(carpeta_principal, 'Credenciales')

os.makedirs(subcarpeta1)
os.makedirs(subcarpeta2)
os.makedirs(subcarpeta3)

print('Carpetas creadas exitosamente.')