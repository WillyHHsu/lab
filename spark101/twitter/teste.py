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


    spark = SparkSession.builder.appName("StructuredNetworkWordCount").getOrCreate()

    userSchema = StructType([
                            StructField("id", LongType(), True),
                            StructField("text", StringType(), True),
                            ])

    df = spark.readStream.schema(userSchema).json('/home/jovyan/git/personal/lab/spark101/twitter/tweets/')
    a =  "/home/jovyan/git/personal/lab/spark101/twitter/twitter/final/final.txt"
    b = "/home/jovyan/git/personal/lab/spark101/twitter/twitter/final/final.txt"
    df.writeStream.format("console").outputMode("append").start().awaitTermination()
