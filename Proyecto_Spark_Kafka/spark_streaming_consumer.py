from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, IntegerType, FloatType

# Configuración de la sesión de Spark
spark = SparkSession.builder.appName("SparkKafkaStreamingConsumer").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

# Esquema de datos para los mensajes entrantes sentores , temnperatudra humdity
schema = StructType([
    StructField("sensor_id", IntegerType()),
    StructField("temperature", FloatType()),
    StructField("humidity", FloatType()),
    StructField("timestamp", IntegerType())
])

# Lee datos en streaming desde Kafka
kafka_df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "sensor_data") \
    .load()

# Procesa los datos JSON
sensor_df = kafka_df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")).select("data.*")

# Muestra los datos en la consola en tiempo real
query = sensor_df.writeStream.outputMode("append").format("console").start()
query.awaitTermination()
