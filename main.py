from ircodec.command import CommandSet

controller = CommandSet('hisense-remote', emitter_gpio=18, receiver_gpio=17, description='Hisense TV Remote')




controller.save_as('hisense-remote.json')
