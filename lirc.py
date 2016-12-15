from subprocess import call

def sendCommand(device, message):
  call(['irsend', 'SEND_ONCE', device, message])
