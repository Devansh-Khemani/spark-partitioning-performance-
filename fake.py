import sys
sys.path.append("libs.zip")

from pyspark.sql import SparkSession
from faker import Faker
import pandas as pd

spark = SparkSession.builder.appName("FakeDataBatchWriter").getOrCreate()
fake = Faker()

total_rows = 10000000
batch_size = 100_000
num_batches = total_rows // batch_size
gcs_output_path = "gs://spark-blog-test/fake-data-spark/"

for batch_num in range(num_batches):
    data = [{
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address(),
        "dob": fake.date_of_birth().isoformat(),
        "company": fake.company()
    } for _ in range(batch_size)]
    
    pdf = pd.DataFrame(data)
    df = spark.createDataFrame(pdf)
    
    print(f"Writing batch {batch_num + 1}/{num_batches} with {batch_size} rows...")
    df.write.mode("append").parquet(gcs_output_path)

print("✅ All batches written successfully.")
