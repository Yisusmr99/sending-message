# Comunicación mediante Paso de Mensajes en Python

Este proyecto muestra un ejemplo básico de comunicación entre procesos usando la técnica de **paso de mensajes** en Python, utilizando el módulo `multiprocessing`.

## Descripción

El programa implementa dos procesos: 

- **Productor**: Genera y envía mensajes a través de una cola.
- **Consumidor**: Recibe y procesa los mensajes de la cola.

Ambos procesos se comunican mediante una **cola** (`Queue`), que actúa como un canal de comunicación seguro entre ellos. Esta demostración ilustra cómo se puede usar la técnica de paso de mensajes para sincronizar y coordinar la ejecución de múltiples procesos.

## Requisitos

- Python 3.x

## Instrucciones de Ejecución

1. Clona este repositorio o copia el código en tu entorno de desarrollo.
2. Ejecuta el script en la terminal o consola de comandos:

    ```bash
    python sending_messages.py
    ```

   Asegúrate de reemplazar `sending_messages.py` con el nombre del archivo en el que guardaste el código.

## Estructura del Código

- **Función `producer(queue)`**: Este es el proceso productor que genera mensajes y los envía a través de la cola `queue`.
- **Función `consumer(queue)`**: Este es el proceso consumidor que recibe los mensajes de la cola `queue` y los procesa.
- **Sincronización de Procesos**:
  - Se usan los métodos `start()` y `join()` para iniciar y sincronizar los procesos.
  - La cola `Queue` garantiza el paso de mensajes de manera segura entre los procesos.

## Explicación del Flujo de Ejecución

1. **Crear los procesos**:
   - Se crea un proceso productor que genera mensajes.
   - Se crea un proceso consumidor que recibe los mensajes.

2. **Iniciar los procesos**:
   - Ambos procesos se ejecutan en paralelo.

3. **Sincronización y Finalización**:
   - El proceso principal espera a que el productor termine de enviar los mensajes.
   - Se envía un mensaje especial `"FIN"` para indicar al consumidor que debe finalizar.
   - Finalmente, el proceso principal espera a que el consumidor termine de procesar todos los mensajes.

## Ejemplo de Salida

Al ejecutar el script, verás una salida similar a la siguiente:

- Produciendo: Mensaje 0 
- Consumiendo: Mensaje 0 
- Produciendo: Mensaje 1 
- Consumiendo: Mensaje 1 
- Produciendo: Mensaje 2 
- Consumiendo: Mensaje 2 
- Produciendo: Mensaje 3 
- Consumiendo: Mensaje 3 
- Produciendo: Mensaje 4 
- Consumiendo: Mensaje 4 
- Todos los procesos han terminado.

## Contribuciones

Si deseas contribuir a este proyecto, siéntete libre de hacer un fork del repositorio y enviar un pull request con tus mejoras o sugerencias.
