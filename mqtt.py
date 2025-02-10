import paho.mqtt.client as mqtt
from ircodec.command import CommandSet
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--host', '-H')
parser.add_argument('--port', '-p', default=1883, type=int)
parser.add_argument('--topic', '-t', default='$SYS/#')
parser.add_argument('remotes', nargs='+')

args = parser.parse_args()

controllers = []
for remote in args.remotes:
    controller = CommandSet(Path(remote).stem, emitter_gpio=18, receiver_gpio=17, description=Path(remote).stem)
    controller.load(remote)
    controllers.append(controller)


def on_connect(client, userdata, flags, reason_code, properties):
    print(f'Connected with result code {reason_code}')
    client.subscribe(args.topic)


def on_message(client, userdata, msg):
    payload = msg.payload.decode('utf-8').lower()
    print(f'{msg.topic} {payload}')
    for controller in controllers:
        if payload == 'power_on':        
            controller.emit('power_on1')
            controller.emit('power_on2')
            controller.emit('power_on3')
        elif payload == 'power_off':
            controller.emit('power_off1')
            controller.emit('power_off2')
            controller.emit('power_off3')
        else:
            controller.emit(payload)


mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect(args.host, args.port, 60)
mqttc.loop_forever(retry_first_connection=True)
