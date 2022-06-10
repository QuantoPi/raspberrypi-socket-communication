# =====================================
# this code goes on your raspberry pi
# =====================================

import socketio
import Adafruit_DHT as dht
from time import sleep

def read_dht11(pin):
    sensor = dht.DHT11
    humidity, temperature = dht.read_retry(sensor, pin)
    return (humidity, temperature)
def main():
    dht_pin = 4
    sio = socketio.Client()
    sio.connect('http://192.168.0.2:3000')
    while(1):
        dht_data = read_dht11(dht_pin)
        data = f"Temperature: {dht_data[0]} Humidity: {dht_data[1]}"
        sio.emit('temp-hum-data', data)
        print("===========================================")
        print("Sending data ...")
        print(data)
        print("===========================================")
        sleep(10)
    sio.disconnect()
if __name__ == '__main__':
   main()