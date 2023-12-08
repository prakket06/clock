import pygame
pygame.init()
my_sound = pygame.mixer.Sound('Over_the_Horizon.mp3')
import time
t = time.localtime(time.time())
localtime = time.asctime(t)
e = str(t.tm_mday)
f = str(t.tm_mon)
g = str(t.tm_year)
print("Today's date is :- " + e + "/" + f + "/" + g)
print()
a, y, z = input("Enter the time for which you want to run the clock in (hh : mm : ss) format :- ").split(" : ")
print()
a = int(a)
y = int(y)
z = int(z)
b = (a * 60 * 60) + (y * 60) + z
c =1.00000000000
for i in range(0, b):
    t = time.localtime(time.time())
    localtime = time.asctime(t)
    x = str(t.tm_sec)
    time.sleep(c)
    if i != (b - 1):
        if len(x) == 2:
            print(t.tm_hour, ":", t.tm_min, ":", x, end='\r')
                  
        elif len(x) == 1:
            print(t.tm_hour, ":", t.tm_min, ": 0" + x, end='\r')
            
    elif i == (b - 1):
        my_sound.play()
        if len(x) == 2:
            print(t.tm_hour, ":", t.tm_min, ":", x, end='\r')
            
        elif len(x) == 1:
            print(t.tm_hour, ":", t.tm_min, ": 0" + x, end='\r')
            
            
