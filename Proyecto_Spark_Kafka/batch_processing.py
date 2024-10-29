from pyspark.sql import SparkSession, functions as F
import time

# Inicializa la sesión de Spark
spark = SparkSession.builder.appName('BatchProcessing').getOrCreate()

# Define la ruta del archivo .csv en HDFS
file_path = 'hdfs://localhost:9000/Tarea3/rows.csv'

# Lee el archivo CSV con cabecera y esquema inferido
df = spark.read.format('csv').option('header', 'true').option('inferSchema', 'true').load(file_path)

# Muestra el esquema de los datos
df.printSchema()

# Muestra las primeras filas del DataFrame
df.show()

# Conteo de prestadores por departamento
conteo_por_departamento = df.groupBy('DepartamentoPrestadorDesc').count()
print("Conteo total de prestadores por departamento:")
conteo_por_departamento.show()
time.sleep(10)

# Lista de nombres de prestadores
print("Lista de nombres de prestadores:")
df.select('NombrePrestador').show()
time.sleep(10)

# Datos organizados por ESE
print("Datos organizados por ESE:")
df.orderBy('ESE').show()
time.sleep(10)

# Ordenar por fecha de corte y por clase de prestador
print("Ordenar por FechaCorte:")
df.orderBy('FechaCorte').show()
print("Ordenar por ClasePrestadorDesc:")
df.orderBy('ClasePrestadorDesc').show()
time.sleep(10)
