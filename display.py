'''display.py = abstraction level above OLED driver ssd1306 or sh1106
(should work for both)
Provides methods
- clear(self)
- text(self, text, x, y)
- write_line(self, text, line)  for writing text
- print(self, text)  works similar to print() serial
- print_s(self, s, separator = '\t')  prints text to more than one line
See examples beow!
'''




class Display():
   
    def __init__(self, oled):     
        self.currentline = 0
        self.maxline = 5
        self.oled = oled
        self.show = oled.show
        self.hline = oled.hline
        self.vline = oled.vline
        self.line = oled.line
        self.rect = oled.rect
        self.fill_rect = oled.fill_rect
        
        
    def clear(self):
        self.oled.fill(0)
        self.currentline = 0
   
    
        
    def text(self, text, x, y):
        self.oled.text(text, x, y)
        
    def write_line(self, text, line):
        '''write text to OLED into line 0...5'''
        self.oled.text(text, 0, line * 10)
        self.oled.show()


    def print(self, text):
        '''print string s to OLED and automatically go to next row
           with clear before line 0'''
        if self.currentline == 0:
            self.oled.fill(0)
        self.write_line(text,  self.currentline )
        self.currentline += 1
        if self.currentline > self.maxline:
            self.currentline = 0
    
    
        
    def print_s(self, s, separator = '\t'):
        '''print string s to OLED
        s -> multiple rows, separated by '\t'   '''
        
        sarray = s.split(separator)
        self.clear()
        self.currentline = 0
        for item in sarray:
            #self.print(item)
            self.text(item, 0, self.currentline * 10)
            self.currentline += 1
            if self.currentline > self.maxline:
                self.currentline = 0
        self.oled.show()    

        
if __name__ == "__main__":
    from machine import Pin, I2C
    import ssd1306, sh1106
    from time import sleep
    
    i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=100000)
    
    width = 128
    height = 64
    
    # Use SSD1306 or SH1106
    #oled = ssd1306.SSD1306_I2C(width, height, i2c)             # this cannot rotate
    oled = sh1106.SH1106_I2C(width, height, i2c, rotate = 180)  # this can rotate 
    
    import time
    
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
        
    
    test_all()
    #test5()

