#!/usr/bin/env python3
from adafruit_extended_bus import ExtendedI2C as I2C

pair = [("ahtx0 temperature, humidity sensor", [0x38]),
        ("bmx temperature, humidity sensor", [0x76,0x77]),
        ("bh1750 light intensity sensor",[0x23]),
        ("sht3x temperature, humidity sensor",[0x44,0x45]),
        ("sgp30 air quality sensor",[0x58]),
        ("sgp40 air quality sensor",[0x59]),
        ("scd30 CO2 sensor",[0x61]),
        ("tsl2561 light intensity sensor",[0x29,0x39,0x49]),
        ("ssd130x display",[0x35,0x36]),
        ("ds1307 RTC",[0x68]),
       ]

#####################################################################################
#
#  The Raspberry Pi I2C buses need to be enabled in /boot/config.txt like this:
#  
#  for I2C-0: # for SDA = GPIO0 (pin 27) and SCL = GPIO1 (pin 28)        - fixed pin #
#  ==========
#  dtparam=i2c_arm=on
#
#  for I2C-1: # for SDA = GPIO2 (pin 3) and SCL = GPIO3 (pin 5)          - fixed pin #
#  ==========
#  dtparam=i2c_vc=on
#
#  for I2c-4  # for SDA = GPIO6 (pin 31) and SCL = GPIO7 (pin 26) - configurable pin #
#  ==========
#  dtoverlay=i2c-gpio,bus=4,i2c_gpio_delayUs=1,i2c_gpio_sda=6,i2c_gpio_scl=7
#
#####################################################################################
i2c0 = I2C(0)
i2c1 = I2C(1)
i2c4 = I2C(4)

def i2c_scan(devices):
    for device in devices:
        for name, addresses in pair:
            for address in addresses:
                if device == address:
                    print("{} device at : {}".format(name, hex(device)))

def main():
    print("Scan i2c-0 bus...")
    devices = i2c0.scan()
    print("i2c devices found on bus 0:",len(devices))
    i2c_scan(devices)

    print("Scan i2c-1 bus...")
    devices = i2c1.scan()
    print("i2c devices found on bus 1:",len(devices))
    i2c_scan(devices)

    print("Scan i2c-4 bus...")
    devices = i2c4.scan()
    print("i2c devices found on bus 4:",len(devices))
    i2c_scan(devices)

if __name__ == "__main__":
    main()
