import asyncio
import random
import time
import concurrent.futures

def consulta_base_datos_remota(numero_consulta):
    # Simula una consulta remota
    inicio = time.perf_counter()  # Medición del tiempo
    espera_segundos = random.uniform(1, 5)
    time.sleep(espera_segundos)  # Bloquea el hilo mientras "responde" la BD
    duracion = time.perf_counter() - inicio
    print(f"Consulta {numero_consulta} finalizada en {duracion:.2f} s")
    return duracion

def simular_con_hilos():
    # Consultas en concurrencia usando hilos (bueno para I/O bloqueante)
    inicio_total = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ejecutor:
        futuros = [ejecutor.submit(consulta_base_datos_remota, i) for i in range(1, 4)]
        for futuro in futuros:
            futuro.result()  # Espera a que termine cada hilo

    duracion_total = time.perf_counter() - inicio_total
    print(f"Tiempo total (hilos): {duracion_total:.2f} s")
    return duracion_total

async def consulta_base_datos_remota_async(numero_consulta: int):
    # Consulta remotacon asyncio 
    inicio = time.perf_counter()
    espera_segundos = random.uniform(1, 5)
    await asyncio.sleep(espera_segundos)  # Cede control al event loop
    duracion = time.perf_counter() - inicio
    print(f"Consulta {numero_consulta} finalizada en {duracion:.2f} s")
    return duracion

def simular_con_asincronia():
    # Lanza 3 tareas async y espera a que terminen juntas
    async def ejecutar() -> float:
        inicio_total = time.perf_counter()

        tareas = [consulta_base_datos_remota_async(i) for i in range(1, 4)]
        await asyncio.gather(*tareas)  # Corre las 3 concurrentemente

        duracion_total = time.perf_counter() - inicio_total
        print(f"Tiempo total (asincronía): {duracion_total:.2f} s")
        return duracion_total

    return asyncio.run(ejecutar())  # Crea y ejecuta el event loop

def simular_con_procesos():
    # Ejecuta 3 consultas en paralelo usando procesos
    inicio_total = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as ejecutor:
        futuros = [ejecutor.submit(consulta_base_datos_remota, i) for i in range(1, 4)]
        for futuro in futuros:
            futuro.result()  # Espera a que termine cada proceso

    duracion_total = time.perf_counter() - inicio_total
    print(f"Tiempo total (procesos): {duracion_total:.2f} s")
    return duracion_total

if __name__ == "__main__":
    # Ejecuta las 3 versiones para comparar tiempos totales
    print("Simulación: 3 consultas")
    simular_con_hilos()
    simular_con_asincronia()
    simular_con_procesos()