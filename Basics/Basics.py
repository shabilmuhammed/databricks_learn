# Databricks notebook source


# COMMAND ----------

# MAGIC %md
# MAGIC # sup

# COMMAND ----------



# COMMAND ----------

# MAGIC %sql
# MAGIC select "sup"

# COMMAND ----------

# MAGIC %run ./includes

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs
# MAGIC ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

files = dbutils.fs.ls("/databricks-datasets/")
display(files)

# COMMAND ----------


