import pandas as pd
import pyfirmata
import time
from time import sleep
sec = 0
data = {'Pulse':'','time':''}
df = pd.DataFrame(data)
port = 'COM3'
board = pyfirmata.Arduino(port)
it = pyfirmata.util.Iterator(board)
it.start()
pirPin = board.get_pin('d:11:i')
a0 = board.get_pin('a:0:i')
print(pirPin)
while True:
    pirData = pirPin.read()
    sleep(1)
    if pirData is not None:
        sec += 1
        potData = a0.read()
        pirData = pirPin.read()

