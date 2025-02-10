#!/usr/bin/python
from ircodec.command import CommandSet
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path")
args = parser.parse_args()

controller = CommandSet.load(args.path)

controller.emit('power')
time.sleep(10)
controller.emit('volume_up')
time.sleep(1)
controller.emit('volume_down')
time.sleep(1)
controller.emit('volume_down')
time.sleep(0.1)
controller.emit('volume_down')
time.sleep(0.1)
controller.emit('volume_down')
time.sleep(0.1)

# for k, v in controller
