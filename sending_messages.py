from multiprocessing import Process, Queue  # Importamos módulos necesarios para trabajar con procesos
import time  # Importamos módulo para manejar tiempos de espera

# Esta función representa el proceso "productor"
def producer(queue):
    """
    Esta función crea mensajes y los envía a otro proceso a través de una 'cola' (queue).
    
    queue: Es una estructura especial (como una fila) para enviar y recibir mensajes.
    """
    for i in range(5):  # Vamos a crear 5 mensajes
        message = f"Mensaje {i}"  # Creamos un mensaje de texto
        print(f"Produciendo: {message}")  # Mostramos en pantalla el mensaje creado
        queue.put(message)  # Enviamos el mensaje a la cola
        time.sleep(1)  # Esperamos 1 segundo antes de crear el siguiente mensaje

# Esta función representa el proceso "consumidor"
def consumer(queue):
    """
    Esta función recibe los mensajes enviados por el productor y los muestra en pantalla.
    
    queue: Es la misma 'cola' utilizada para recibir los mensajes.
    """
    while True:  # Repetir infinitamente hasta que llegue un mensaje especial
        message = queue.get()  # Recibimos un mensaje de la cola (espera hasta que haya un mensaje)
        if message == "FIN":  # Si el mensaje recibido es "FIN", terminamos este proceso
            break  # Salimos del bucle
        print(f"Consumiendo: {message}")  # Mostramos en pantalla el mensaje recibido
        time.sleep(2)  # Esperamos 2 segundos antes de recibir el siguiente mensaje

# Esta parte del código solo se ejecuta si ejecutamos este archivo directamente
if __name__ == "__main__":
    # Creamos una cola que permitirá a los procesos enviar y recibir mensajes
    message_queue = Queue()

    # Creamos el proceso productor que generará mensajes
    producer_process = Process(target=producer, args=(message_queue,))
    
    # Creamos el proceso consumidor que recibirá los mensajes
    consumer_process = Process(target=consumer, args=(message_queue,))

    # Iniciamos ambos procesos
    producer_process.start()  # Inicia el proceso productor
    consumer_process.start()  # Inicia el proceso consumidor

    # Esperamos a que el proceso productor termine de enviar todos sus mensajes
    producer_process.join()

    # Enviamos un mensaje especial de "FIN" para que el proceso consumidor sepa que debe terminar
    message_queue.put("FIN")

    # Esperamos a que el proceso consumidor termine de recibir y procesar todos los mensajes
    consumer_process.join()

    print("Todos los procesos han terminado.")  # Mensaje final indicando que todos los procesos han terminado