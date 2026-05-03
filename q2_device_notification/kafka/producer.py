import json
from aiokafka import AIOKafkaProducer

KAFKA_BROKER = "localhost:9092"       # ← Kafka server address
TOPIC = "device-config-notifications" # ← Topic where notifications will be sent


async def send_notification(payload: dict):
    """
    One JSON message is published to the Kafka topic.
    Producer → Kafka Topic → Consumer reads and alerts the user
    """
    producer = AIOKafkaProducer(bootstrap_servers=KAFKA_BROKER)
    await producer.start()
    try:
        message = json.dumps(payload).encode("utf-8")
        await producer.send_and_wait(TOPIC, message)
        print(f"📤 Send on Kafka: {payload}")
    except Exception as e:
        print(f"❌ Kafka error: {e}")
        raise e
    finally:
        await producer.stop()
