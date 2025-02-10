from ircodec.command import CommandSet

controller = CommandSet('hisense-remote', emitter_gpio=18, receiver_gpio=17, description='Hisense TV Remote')

print('Press the power button on remote')
controller.add('power')

print('Press the Volume+ button on remote...')
controller.add('volume_up')

print('Press the Volume- button on remote')
controller.add('volume_down')


controller.save_as('hisense-remote.json')
