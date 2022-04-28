"""
from kafka import KafkaConsumer

if __name__ == "__main__":

    consumer = KafkaConsumer(

            "user.registrations",
            bootstrap_servers=['0.0.0.0:9092'],
            auto_offset_reset="latest",
            enable_auto_commit=True,
            group_id="tech-core-easy-1",
            )
    def Hj():
        for message in consumer:
            return (message)
"""