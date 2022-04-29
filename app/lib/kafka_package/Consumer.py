from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "user.registrations",
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset="latest",
    enable_auto_commit=True,
    group_id="test-consumer-group",
    )

ls=""
for message in consumer:
    mg="Got ".format(json.dumps(message.value))
    ls+=str(mg)
def consumer_function():     
    return ls