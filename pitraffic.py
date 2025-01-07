from gpiozero import LED
from time import sleep
from datetime import datetime
import random
import sys

# North Bound Lights
# Define GPIO Pins
nbred = LED(16)
nbyellow = LED(20)
nbgreen = LED(21)
nbdontwalk = LED(24)
nbwalk = LED(23)

# NB Variables
nbmintime = 10
nbmaxtime = 20
nbpedcycle = 7
nbpedclear = 15
nbyellowclear = 3

# West Bound Lights
# Define GPIO Pins
wbred = LED(13)
wbyellow = LED(19)
wbgreen = LED(26)
wbdontwalk = LED(6)
wbwalk = LED(5)

# WB Variables
wbmintime = 10
wbmaxtime = 20
wbpedcycle = 7
wbpedclear = 32
wbyellowclear = 3

# Globals
redoverlap = 2

while True:
  # datetime object containing current date and time
  now = datetime.now()

  # dd/mm/YY H:M:S
  dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
  dr_string = now.strftime("%H")
  print("date and time =", dt_string)
  #print("hour =", dr_string)

  if dr_string == 13:
    print("flash loop because hour is", dr_string)
    # Go into flash
    nbred.on()
    wbred.off()
    sleep(0.50)
    nbred.off()
    wbred.on()
    sleep(0.50)
    dr_string = now.strftime("%H")
  else:  
    print("normal loop because hour is", dr_string)
    # Start Up
    nbred.on()
    nbyellow.off()
    nbgreen.off()
    nbdontwalk.on()
    nbwalk.off()

    wbred.on()
    wbyellow.off()
    wbgreen.off()
    wbdontwalk.on()
    wbwalk.off()
  
    for i in range(redoverlap,-1,-1):
       sys.stdout.write("\r")
       sys.stdout.write("red overlap for {:2d} seconds.".format(i))
       sys.stdout.flush()
       sleep(1)

    wbred.off()
    wbyellow.off()
    wbgreen.on()

    wbwalkcall = random.randint(0,1)

    # We have decided to cross the intersection
    if wbwalkcall == 1:
      print("\rwb green");
      wbdontwalk.off()
      wbwalk.on()
      for i in range(wbpedcycle,-1,-1):
         sys.stdout.write("\r")
         sys.stdout.write("wb walk for {:2d} seconds.".format(i))
         sys.stdout.flush()
         sleep(1)
      wbwalk.off()
      wbdontwalk.on()
      for i in range(wbpedclear,-1,-1):
         sys.stdout.write("\r")
         sys.stdout.write("wb ped clear for {:2d} seconds.".format(i))
         sys.stdout.flush()
         wbdontwalk.off()
         sleep(0.50)
         wbdontwalk.on()
         sleep(0.50)
    else:
       wbdontwalk.on()
       wbwalk.off()
       sleeptime = random.randint(wbmintime, wbmaxtime)
       for i in range(sleeptime,-1,-1):
         sys.stdout.write("\r")
         sys.stdout.write("wb green for {:2d} seconds.".format(i))
         sys.stdout.flush()
         sleep(1)

    wbred.off()
    wbyellow.on()
    wbgreen.off()

    for i in range(wbyellowclear,-1,-1):
       sys.stdout.write("\r")
       sys.stdout.write("wb yellow for {:2d} seconds.".format(i))
       sys.stdout.flush()
       sleep(1)

    wbred.on()
    wbyellow.off()
    wbgreen.off()

    for i in range(redoverlap,-1,-1):
       sys.stdout.write("\r")
       sys.stdout.write("red overlap for {:2d} seconds.".format(i))
       sys.stdout.flush()
       sleep(1)

    nbred.off()
    nbyellow.off()
    nbgreen.on()

    nbwalkcall = random.randint(0,1)

    # We have decided to cross the intersection
    if nbwalkcall == 1:
      print("\rnb green")
      nbdontwalk.off()
      nbwalk.on()
      for i in range(nbpedcycle,-1,-1):
         sys.stdout.write("\r")
         sys.stdout.write("nb walk for {:2d} seconds.".format(i))
         sys.stdout.flush()
         sleep(1)
      nbwalk.off()
      nbdontwalk.on()
      for i in range(nbpedclear,-1,-1):
        sys.stdout.write("\r")
        sys.stdout.write("nb ped clear {:2d}".format(i))
        sys.stdout.flush()
        nbdontwalk.off()
        sleep(0.50)
        nbdontwalk.on()
        sleep(0.50)
    else:
      nbdontwalk.on()
      nbwalk.off()
      sleeptime = random.randint(nbmintime, nbmaxtime)
      for i in range(sleeptime,-1,-1):
         sys.stdout.write("\r")
         sys.stdout.write("nb rest for {:2d} seconds.".format(i))
         sys.stdout.flush()
         sleep(1)

    nbred.off()
    nbyellow.on()
    nbgreen.off()

    for i in range(nbyellowclear,-1,-1):
       sys.stdout.write("\r")
       sys.stdout.write("nb yellow for {:2d} seconds.".format(i))
       sys.stdout.flush()
       sleep(1)

    nbred.on()
    nbyellow.off()
    nbgreen.off()

    # End Loop
