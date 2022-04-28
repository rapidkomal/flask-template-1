from kafka import KafkaConsumer

import sys

bootstrap_servers = ['0.0.0.0:9092']

topicName = 'users.verifications'

consumer = KafkaConsumer (topicName, group_id ='tech-core-easy-1',bootstrap_servers =
   bootstrap_servers)

for msg in consumer:
    print("Topic Name=%s,Message=%s"%(msg.topic,msg.value))

sys.exit()
