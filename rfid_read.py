from time import sleep_ms
from machine import Pin, SoftSPI
from mfrc522 import MFRC522

sck = Pin(13)
mosi = Pin(2)
miso = Pin(15)
spi = SoftSPI(sck=sck, mosi=mosi, miso=miso)

sda = Pin(21)
print('test')

while True:


    rdr = MFRC522(spi, sda)
    uid = ""
    (stat, tag_type) = rdr.request(rdr.REQIDL)
    if stat == rdr.OK:
        (stat, raw_uid) = rdr.anticoll()
        if stat == rdr.OK:
            uid = ("0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
            print(uid)
            sleep_ms(100)
