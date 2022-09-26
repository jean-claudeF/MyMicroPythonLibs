from machine import Pin, I2C

print("I2C0 [8, 9]:")
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=100000)
addresses = i2c.scan()
for a in addresses:
    print(hex(a))

print()
print("I2C0 [16, 17]:")
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=100000)
addresses = i2c.scan()
for a in addresses:
    print(hex(a))
    
print()
print("I2C1 [6,7]:")
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=100000)
addresses = i2c.scan()
for a in addresses:
    print(hex(a))
    
print()
print("I2C1 [18,19]:")
i2c = I2C(1, scl=Pin(19), sda=Pin(18), freq=100000)
addresses = i2c.scan()
for a in addresses:
    print(hex(a))    