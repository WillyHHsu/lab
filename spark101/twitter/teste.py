#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 16:55:00 2019

@author: willy
"""

if __name__ == '__main__':
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import explode
    from pyspark.sql.functions import split
    from pyspark.sql.types import StructType, StructField, StringType, LongType
    import findspark

    """
    spark = SparkSession.builder.appName("StructuredNetworkWordCount").getOrCreate()
    
    schmaA=spark.read.format("json").load("/home/jovyan/git/personal/lab/spark101/twitter/tweets/1110288120791093251.json").schema
    userSchema = StructType().add("id", "integer").add("text", "string")
    df = spark.readStream.schema(schmaA).json('/home/jovyan/git/personal/lab/spark101/twitter/tweets/')
    
    df.writeStream.format("csv").outputMode("append").option("final.csv",'/home/jovyan/git/personal/lab/spark101/twitter/final').start().awaitTermination()
    groupDF = df.select("id").groupBy("id").count()
    
    groupDF.writeStream.format("csv").outputMode("append").option("/home/jovyan/git/personal/lab/spark101/twitter/final/final.csv").start().awaitTermination()
    """
    
    spark = SparkSession.builder.appName("StructuredNetworkWordCount").getOrCreate()
    
    userSchema  = StructType([
                            StructField("id", LongType(), True),
                            StructField("text", StringType(), True),
                            ])
    
    df = spark.readStream.schema(userSchema).json('/home/jovyan/git/personal/lab/spark101/twitter/tweets/')
    df.writeStream.format("console").outputMode("append").start().awaitTermination()
