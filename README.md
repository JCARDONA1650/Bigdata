# Bigdata
Tarea 3 Procesamiento de Datos con Apache Spark_Grupo_43

# Proyecto de Procesamiento de Datos con Apache Spark y Kafka

Este proyecto realiza procesamiento de datos en dos modalidades:
1. **Procesamiento Batch** con `batch_processing.py`: Analiza datos de salud en formato CSV usando Spark.
2. **Procesamiento en Tiempo Real** con `spark_streaming_consumer.py`: Consume y procesa datos en tiempo real desde Kafka usando Spark Streaming.

El objetivo es procesar un conjunto de datos de salud en Colombia tanto en tiempo real como en lotes, ayudando a organizar y analizar la información de prestadores de servicios de salud de bases de gran volumen para manejo de BIG DATA.

## Contenido del Repositorio

- `batch_processing.py`: Código para el procesamiento batch en Spark.
- `spark_streaming_consumer.py`: Consumidor en Spark Streaming que se conecta a Kafka para procesar datos de sensores en tiempo real.
- `README.md`: Explicación del proyecto y las instrucciones de uso.

---

## Requisitos Previos

1. **Instalación de Apache Spark y Kafka** en una máquina virtual (o en un entorno local).
2. **Acceso a Hadoop HDFS** para el almacenamiento de datos.
3. **Python 3.x** y el paquete `pyspark` instalado:
   ```bash
   pip install pyspark
