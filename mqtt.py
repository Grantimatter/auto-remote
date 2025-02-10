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
    controller = CommandSet.load(remote)
    controllers.append(controller)


def on_connect(client, userdata, flags, reason_code, properties):
    print(f'Connected with result code {reason_code}')
    client.subscribe(args.topic)


def on_message(client, userdata, msg):
    payload = msg.payload.decode('utf-8').lower()
    print(f'{msg.topic} {payload}')
    for controller in controllers:
        try:
            if payload == 'power_on':        
                controller.emit('power_on1')
                controller.emit('power_on2')
                print('Emitting Power ON')
            elif payload == 'power_off':
                controller.emit('power_off1')
                controller.emit('power_off2')
                print('Emitting Power OFF')
            else:
                controller.emit(payload)
                print(f'Emitting {payload.upper()}')
        except Exception as e:
            print(f'Error emitting {payload}: {e}')


mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect(args.host, args.port, 60)
mqttc.loop_forever(retry_first_connection=True)
