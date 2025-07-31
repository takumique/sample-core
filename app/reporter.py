import json

import paho.mqtt.client as mqtt

import log


class Reporter:

    def __init__(
        self,
        addr,
        port,
    ):
        self.addr = addr
        self.port = port

    def publish(
        self,
        topic,
        payload,
    ):
        def on_connect_fn(client, userdata, flags, reason_code, properties):
            client.publish(topic, payload)
        client = mqtt.Client(callback_api_version = mqtt.CallbackAPIVersion.VERSION2)
        try:
            log.info(f"Connecting to {self.addr}:{self.port}")
            client.on_connect = on_connect_fn
            client.connect(self.addr, self.port)
            client.disconnect()
        except Exception as e:
            log.exception(e)

    def publish_api_server_state(
        self,
        server_state,
    ):
        topic = "ui/state"
        payload = {
            "api": server_state,
        }
        self.publish(
            topic,
            json.dumps(payload),
        )
        log.info(f"Published: {server_state}")

    def publish_core_server_state(
        self,
        server_state,
    ):
        topic = "ui/state"
        payload = {
            "core": server_state,
        }
        self.publish(
            topic,
            json.dumps(payload),
        )
        log.info(f"Published: {server_state}")
