from pyspark.sql import SparkSession
from pyspark.sql.functions import hash

# Initialize Spark session
spark = SparkSession.builder.appName("Deterministic1PercentFilter").getOrCreate()

# Paths
input_path = "gs://<your-bucket-name>/fake-data-spark/"
output_path = "gs://<your-bucket-name>/fake-data-spark-1percent/"

# Read full dataset
df = spark.read.parquet(input_path)

# Filter 1% of data using hash of 'email' column
filtered_df = df.filter((hash("email") % 100) == 0)

# Coalesce and write
filtered_df.coalesce(1).write.mode("overwrite").parquet(output_path)

print("✅ 1% of data filtered using 'email' column and written to:", output_path)
