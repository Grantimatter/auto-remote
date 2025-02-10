from ircodec.command import CommandSet
import time

controller = CommandSet.load('hisense-remote.json')


controller.emit('power')
time.sleep(10)
controller.emit('volume_up')
time.sleep(0.1)
controller.emit('volume_down')
time.sleep(0.1)
controller.emit('volume_down')
time.sleep(0.1)
controller.emit('volume_down')
time.sleep(0.1)
controller.emit('volume_down')
time.sleep(0.1)

# for k, v in controller
