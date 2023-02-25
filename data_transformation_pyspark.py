from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.functions import monotonically_increasing_id
from pyspark.sql.functions import concat, col
from pyspark.sql.functions import input_file_name, udf
from pyspark.sql.types import StringType

my_conf = SparkConf()
my_conf.set("spark.app.name", "my first application")
my_conf.set("spark.master","local[*]")

spark = SparkSession.builder.config(conf=my_conf).getOrCreate()

serp_schema = StructType([
    StructField("id", StringType(), False),
    StructField("file_id", StringType(), False),
    StructField("domain", StringType(), False),
    StructField("position", IntegerType(), False),
    StructField("category", StringType(), False),
    StructField("query", StringType(), False),
    StructField("url", StringType(), False),
])

# Define a UDF to extract the filename from the file path
get_filename = udf(lambda x: x.split("/")[-1], StringType())

path = r"F:\desktop backup august12021\21WORK\automate_boring_stuff\2023\RELIANCE_WEBSITE_RANK_SEO\sparkbark\ranked_files\*.csv"

unioned_df = spark.read.format("csv") \
    .option("header", "true") \
    .schema(serp_schema)\
    .option("path", path) \
    .load()

unioned_df.createOrReplaceTempView("unioned_table")

output_df=spark.sql(""" SELECT category,domain,position as Rank,COUNT(*) as Rank_Count FROM unioned_table
          GROUP BY category,domain,position
          ORDER BY category,domain,position
          """)

output_df=output_df.coalesce(1)
output_df.write\
.format("csv")\
.mode("overwrite")\
.option("maxRecordsPerFile", 100000)\
.save("output_files")


