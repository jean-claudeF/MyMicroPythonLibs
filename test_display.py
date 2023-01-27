'''display.py = abstraction level above OLED driver ssd1306 or sh1106'''

from display import Display

from machine import Pin, I2C
import ssd1306
import sh1106
from time import sleep
import time

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=100000)

width = 128
height = 64
#oled = ssd1306.SSD1306_I2C(width, height, i2c)
oled = sh1106.SH1106_I2C(width, height, i2c)

display = Display(oled)

def test1():
    display.clear()
    display.print("TEST OLED PRINT")
    for i in range(0,8):
        #oled.print_line("TEST " + str(i))
        display.print("TEST " + str(i))
        ##time.sleep(0.2)
        ##display.show()

def test2():
    display.clear()

    display.text("TEST OLED", 0, 0)      # text, x, y, colour (1 = white)     
    #display.text("TEST OLED",5,5)
    display.text("by JCF",5,15)
    display.text("Another row", 5, 25)
    display.text("Yet another row", 5, 35)
    display.text("And one more", 5, 45)
    display.show()



def test3():
    display.clear()
    display.text("TEST ", 30, 0)             
    display.hline(10,10, 20, 1)
    display.vline(10, 20, 30, 1)
    display.line(10, 10, 50, 50, 1)
    display.rect(20, 20, 60, 40, 1)
    display.fill_rect(80, 20, 20, 20, 1)
    display.show()



def test4():
    display.clear()
    for i in range(0,6):
        #display.print_line("TEST LINE" + str(i))
        display.print("TEST LINE" + str(i))
    display.show()               

def test5():
    s = "Hello \t world \t ! \t 3.14     \t The answer is \t 42"
    display.print_s(s)
    
    time.sleep(1)
    s = "123456789 \t ! \t 3.14     \t The answer is \t 42\t Hitchhiker"
    display.print_s(s) 
    
    
def test_all():
    test1()
    time.sleep(1)
    test2()
    time.sleep(1)
    test3()
    time.sleep(1)
    test4()
    time.sleep(1)
    test5()
    time.sleep(1)
    
print("Look at display!")
print("Running tests")

test_all()
#test5()

