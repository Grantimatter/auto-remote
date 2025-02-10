from ircodec.command import CommandSet
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('name')
args = parser.parse_args()

controller = CommandSet(args.name, emitter_gpio=18, receiver_gpio=17, description=args.name)

print('Press the power button on remote')
controller.add('power')

print('Press the Volume+ button on remote...')
controller.add('volume_up')

print('Press the Volume- button on remote')
controller.add('volume_down')


controller.save_as(f'{args.name}.json')
