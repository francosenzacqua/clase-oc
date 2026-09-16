# Escribe tu código aquí debajo 👇

# 1. Definir año actual
anio_actual = 2026

# 2. Pedir año de nacimiento (recuerda convertir a int)
nac = input("¿En que año naciste? ")
añonac = int(nac)  # Convertimos texto a número

# 3. Calcular edad
añonac = anio_actual - añonac
print("Tienes:", añonac)

# 4. Condicional If / Else
if añonac > 18:
    print("🔥 ¡Podes pasar")
elif añonac < 18:
    print("No podes pasar")