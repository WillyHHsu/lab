from pyspark import SparkContext,SparkConf
from pyspark.streaming import StreamingContext
import json
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql import SQLContext
import findspark

path = "/home/jovyan/git/personal/lab/spark101/twitter/tweets/"

conf = (SparkConf()
        .setMaster("local[*]")
        .set("spark.executor.memory", "1g")
        .setAppName('teste'))

sc = SparkContext(conf = conf)
sql = SQLContext(sc)
ssc = StreamingContext(sc, 10) #seconds
tweets_stream = ssc.textFileStream(path)
####

tweet = tweets_stream.map(lambda x:x)
#tweet.foreachRDD(lambda rdd: json.load(rdd))
tweet.pprint()

###

###
tweet.saveAsTextFiles('/home/jovyan/git/personal/lab/spark101/twitter/final/algo', 'teste')
#salva com um nome prefixo e sufixo, rode para entender exe: ficará algo_numero_gigante_teste

ssc.start()
ssc.awaitTermination()