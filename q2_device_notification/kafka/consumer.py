import json
import asyncio
from aiokafka import AIOKafkaConsumer

KAFKA_BROKER = "localhost:9092"
TOPIC = "device-config-notifications"


async def consume_notifications():
    """
    Kafka is listening to the topic and whenever a message arrives, it processes the message.
    In a real project: send WebSocket or Email notifications to the user
    
    """
    consumer = AIOKafkaConsumer(
        TOPIC,
        bootstrap_servers=KAFKA_BROKER,
        group_id="device-notification-group",
        auto_offset_reset="earliest"
    )
    await consumer.start()
    print(f"👂 Kafka consumer is listening to the topic: {TOPIC}")

    try:
        async for msg in consumer:
            data = json.loads(msg.value.decode("utf-8"))
            print(f"\n🔔 NOTIFICATION Reached!")
            print(f"   Device ID  : {data['device_id']}")
            print(f"   Device IP  : {data['device_ip']}")
            print(f"   Details    : {data['device_details']}")
            print(f"   Alert      : {data['alert']}")
            print("-" * 40)

            # 👇 Here you can send WebSocket or Email notifications to the user
            # await send_email(data)
            # await send_sms(data)

    finally:
        await consumer.stop()



if __name__ == "__main__":
    asyncio.run(consume_notifications())
