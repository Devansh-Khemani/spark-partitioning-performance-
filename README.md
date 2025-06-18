# spark-partitioning-performance-
# 🚀 Spark Partitioning Performance: Repartition vs Coalesce (on Google Cloud Dataproc)

This repository demonstrates the performance comparison between `repartition()` and `coalesce()` transformations in Apache Spark using real-world batch jobs on **Google Cloud Dataproc**.

We process a large fake dataset (~5–6 million rows), filter 1% of it, and write it to Parquet using both `repartition(1)` and `coalesce(1)`. The test is done using Dataproc batch jobs to analyze real execution times and task distributions.

---

## 📁 Repository Structure


.
├── fake.py         # Generates fake data with 5–6 million rows
├── repartition.py   # Filters 1% and writes using repartition(1)
├── coalesce.py      # Filters 1% and writes using coalesce(1)
└── README.md


1. 🔧 Create a Dataproc Batch

gcloud dataproc batches submit pyspark gs://spark-blog-test/code/fake.py \
  --batch=generate-fake-data-batch \
  --region=us-central1 \
  --version=2.1 \
  --deps-bucket=spark-blog-test \
  --subnet=default \
  --py-files=gs://spark-blog-test/code/libs.zip

2. 🌀 Filter and Write with repartition(1)

gcloud dataproc batches submit pyspark gs://<your-bucket-name>/code/repartition.py \
  --batch=filter-repartition-batch \
  --region=us-central1 \
  --version=2.1 \
  --deps-bucket=<your-bucket-name> \
  --subnet=default

3. 🌀 Filter and Write with coalesce(1)

gcloud dataproc batches submit pyspark gs://<your-bucket-name>/code/coalesce.py \
  --batch=filter-coalesce-batch \
  --region=us-central1 \
  --version=2.1 \
  --deps-bucket=<your-bucket-name> \
  --subnet=default




