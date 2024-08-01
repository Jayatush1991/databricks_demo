# Databricks notebook source
print("Hello World")

# COMMAND ----------

# MAGIC
# MAGIC %sql 
# MAGIC SELECT "Hello world from SQL!"

# COMMAND ----------

# MAGIC %md
# MAGIC #Tittle 1
# MAGIC ## Title 2
# MAGIC ### Title 3
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %run /Workspace/Includes/Setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls('databricks-datasets')
print(files)

# COMMAND ----------

display(files)
