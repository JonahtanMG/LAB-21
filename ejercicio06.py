import json
equipos_futbol = [
    {
        "Nombre": "Real Madrid",
        "país": "España",
        "nivelAtaque": 92,
        "nivelDefensa": 88
    },
    {
        "Nombre": "Barcelona",
        "país": "España",
        "nivelAtaque": 90,
        "nivelDefensa": 86
    }
]

json_formateado = json.dumps(equipos_futbol, indent=4, ensure_ascii=False)

print("Lista de los equipos")
print(json_formateado)