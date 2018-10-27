from pyspark import sql, SparkConf, SparkContext
import pyspark
import os

conf = SparkConf().setAppName("Read_CSV")
sc = SparkContext(conf=conf)
spark = sql.SQLContext(sc)

df1 = spark.read.option("delimiter", ";").option("header", "true").option("encoding", "ISO-8859-1").csv(
    "/home/data/Documents/dadosCvm/Cias Abertas Documentos Formulário DFP - Balanço Patrimonial Passivo (BPP)/Cias Abertas Documentos Formulário DFP - Balanço Patrimonial Passivo (BPP)/bpp_cia_aberta_con_2013.csv")

for i in range(0,3):
    df2 = spark.read.option("delimiter", ";").option("header", "true").option("encoding", "ISO-8859-1").csv(
        "/home/data/Documents/dadosCvm/Cias Abertas Documentos Formulário DFP - Balanço Patrimonial Passivo (BPP)/Cias Abertas Documentos Formulário DFP - Balanço Patrimonial Passivo (BPP)/bpp_cia_aberta_con_2013.csv")
    df1 = df1.union(df2)

df1.show()

print(df1.count())