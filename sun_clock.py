from datetime import datetime
import time
import pytz
from astral import LocationInfo, moon
from astral.sun import sun
import board
import neopixel

# INIZIALIZZO I LED
pixel_pin = board.D12
num_pixels = 60

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.15, auto_write=False,pixel_order=neopixel.RGB)

# COLORI
OFF = (0,0,0)

CIELO_AZZURRO = (10, 27, 33)
CIELO_AZZURRO_1 = (15, 40, 50)
CIELO_TRAMONTO = (30, 10, 3)
CIELO_ALBA = (80, 25, 9)
CIELO_LUNA = (0, 0, 7)

TRAMONTO_00 = (250, 90, 15)
TRAMONTO_0 = (250, 70, 15)
TRAMONTO_1 = (255, 40, 10)
TRAMONTO_2 = (245, 70, 12)
TRAMONTO_3 = (240, 65, 10)
TRAMONTO_4 = (235, 48, 8)
TRAMONTO_5 = (210, 33, 12)
TRAMONTO_6 = (230, 148, 75)
TRAMONTO_7 = (203, 120, 107)
TRAMONTO_8 = (139, 104, 119)
TRAMONTO_9 = (103, 82, 124)
TRAMONTO_10 = (72, 61, 117)
TRAMONTO_11 = (40, 38, 103)
TRAMONTO_12 = (14, 19, 90)
TRAMONTO_13 = (0, 5, 71)
TRAMONTO_14 = (0, 0, 51)
TRAMONTO_15 = (0, 0, 40)
TRAMONTO_16 = (0, 0, 12)

# LAT E LONG PER BOLZANO
city = LocationInfo("Rome", "Italy", "Europe/Rome", 46.489650, 11.331729)

def getDuration(then, now = datetime.now(), interval = "default"):

    # Returns a duration as specified by variable interval
    # Functions, except totalDuration, returns [quotient, remainder]

    duration = now - then # For build-in functions
    duration_in_s = duration.total_seconds() 

    def years():
      return divmod(duration_in_s, 31536000) # Seconds in a year=31536000.

    def days(seconds = None):
      return divmod(seconds if seconds != None else duration_in_s, 86400) # Seconds in a day = 86400

    def hours(seconds = None):
      return divmod(seconds if seconds != None else duration_in_s, 3600) # Seconds in an hour = 3600

    def minutes(seconds = None):
      return divmod(seconds if seconds != None else duration_in_s, 60) # Seconds in a minute = 60

    def seconds(seconds = None):
      if seconds != None:
        return divmod(seconds, 1)   
      return duration_in_s

    def totalDuration():
        y = years()
        d = days(y[1]) # Use remainder to calculate next variable
        h = hours(d[1])
        m = minutes(h[1])
        s = seconds(m[1])

        return "Time between dates: {} years, {} days, {} hours, {} minutes and {} seconds".format(int(y[0]), int(d[0]), int(h[0]), int(m[0]), int(s[0]))

    return {
        'years': int(years()[0]),
        'days': int(days()[0]),
        'hours': int(hours()[0]),
        'minutes': int(minutes()[0]),
        'seconds': int(seconds()),
        'default': totalDuration()
    }[interval]


while True:
   # QUASI QUASI TANTO VALE DEFINIRE UN TOT_PIXEL TANTO è SEMPRE 30
   tot_pixel_sole = 30
   tot_pixel_luna = 30

   s = sun(city.observer, date=datetime.now(), tzinfo=city.timezone)
   alba = s["sunrise"]
   tramonto = s["sunset"]

   delta_tot_sole = getDuration(alba, tramonto, 'minutes')
   adesso = datetime.now(pytz.timezone('Europe/Rome'))
   
   # RESET LEDs
   pixels.fill(OFF)
   pixels.show()

   # CALCOLO A SECONDA DELLA FASE DEL GIORNO
   if (alba <= adesso <= tramonto):
      delta_sole = getDuration(alba, adesso, 'minutes')
      perc_sole = (delta_sole / delta_tot_sole) * 100
      perc_sole = round(perc_sole, 2)
      pixel_sole = (tot_pixel_sole * perc_sole) / 100
      pixel_sole =  round(pixel_sole) -1
      print ("perc sole -->", perc_sole)
      print("pixel sole -->", pixel_sole)
      
      #pixels.fill(cielo)
      #pixels.show()
      #pixels[pixel_sole] = (255, 255, 0)
      #pixels.show()
      
      #pixel_sole = 28
            
      
      # PER DECIDERE LA SFUMATURA IN BASE ALLA POSIZIONE DEL SOLE
      if (0<= pixel_sole <= 3):
         
         for i in range(tot_pixel_sole):
            pixels[i] = CIELO_TRAMONTO
            #pixels.show()
            
         pixels[pixel_sole] = (255, 102, 102)
         pixels[pixel_sole + 1] = (255, 102, 102)
         pixels.show()
      
      if (4<= pixel_sole <= 10):

         pixels.brightness = 0.2

         for i in range(tot_pixel_sole):
            pixels[i] = CIELO_AZZURRO
            #pixels.show()
            
         
         pixels[pixel_sole] = (255, 255, 0)
         pixels[pixel_sole + 1] = (255, 255, 25)
         pixels[pixel_sole - 1] = (255, 255, 25)
         pixels.show()

      if (10<= pixel_sole <= 20):

         pixels.brightness = 0.4

         for i in range(tot_pixel_sole):
            pixels[i] = CIELO_AZZURRO
            #pixels.show()
            
         
         pixels[pixel_sole] = (255, 255, 0)
         pixels[pixel_sole + 1] = (255, 255, 25)
         pixels[pixel_sole - 1] = (255, 255, 25)
         pixels.show()   

      if (20<= pixel_sole <= 26):

         pixels.brightness = 0.25

         for i in range(tot_pixel_sole):
            pixels[i] = CIELO_AZZURRO
            #pixels.show()
            
         
         pixels[pixel_sole] = (255, 255, 0)
         pixels[pixel_sole + 1] = (255, 255, 25)
         pixels[pixel_sole - 1] = (255, 255, 25)
         pixels.show()      
 
      if (pixel_sole == 27):

         pixels.brightness = 0.18
         
         for i in range(tot_pixel_sole):
            pixels[i] = TRAMONTO_16
            #pixels.show()

         pixels[pixel_sole] = TRAMONTO_1
         pixels[pixel_sole - 1] = TRAMONTO_2
         pixels[pixel_sole - 2] = TRAMONTO_3
         pixels[pixel_sole - 3] = TRAMONTO_4
         pixels[pixel_sole - 4] = TRAMONTO_5
         pixels[pixel_sole - 5] = TRAMONTO_6
         pixels[pixel_sole - 6] = TRAMONTO_7
         pixels[pixel_sole - 7] = TRAMONTO_8
         pixels[pixel_sole - 8] = TRAMONTO_9
         pixels[pixel_sole - 9] = TRAMONTO_10
         pixels[pixel_sole - 10] = TRAMONTO_11
         pixels[pixel_sole - 11] = TRAMONTO_12
         pixels[pixel_sole - 12] = TRAMONTO_13
         pixels[pixel_sole - 13] = TRAMONTO_14
         pixels[pixel_sole - 14] = TRAMONTO_15
         
         pixels[pixel_sole + 1] = TRAMONTO_0
         #pixels[pixel_sole + 2] = TRAMONTO_00
         
         pixels.show()

      if (pixel_sole == 28):

         pixels.brightness = 0.15

         for i in range(tot_pixel_sole):
            pixels[i] = TRAMONTO_16
            #pixels.show()

         pixels[pixel_sole] = TRAMONTO_4
         pixels[pixel_sole - 1] = TRAMONTO_5
         pixels[pixel_sole - 2] = TRAMONTO_6
         pixels[pixel_sole - 3] = TRAMONTO_9
         pixels[pixel_sole - 4] = TRAMONTO_10
         pixels[pixel_sole - 5] = TRAMONTO_11
         pixels[pixel_sole - 6] = TRAMONTO_12
         pixels[pixel_sole - 7] = TRAMONTO_13
         pixels[pixel_sole - 8] = TRAMONTO_14
         pixels[pixel_sole - 9] = TRAMONTO_15
                 
         pixels[pixel_sole + 1] = TRAMONTO_0
         
         pixels.show()

      if (pixel_sole == 29):

         pixels.brightness = 0.12
         
         for i in range(tot_pixel_sole):
            pixels[i] = TRAMONTO_16
            #pixels.show()

         pixels[pixel_sole] = TRAMONTO_5
         pixels[pixel_sole - 1] = TRAMONTO_8
         pixels[pixel_sole - 2] = TRAMONTO_9
         pixels[pixel_sole - 3] = TRAMONTO_11
         pixels[pixel_sole - 4] = TRAMONTO_12
         pixels[pixel_sole - 5] = TRAMONTO_13
         pixels[pixel_sole - 6] = TRAMONTO_14
         pixels[pixel_sole - 7] = TRAMONTO_15
         pixels[pixel_sole - 8] = TRAMONTO_15
         #pixels[pixel_sole - 9] = TRAMONTO_16
         
         pixels.show()
      

   else:
      delta_tot_luna = 1440 - delta_tot_sole
      delta_luna = getDuration(tramonto, adesso, 'minutes')
      perc_luna = (delta_luna / delta_tot_luna) * 100
      perc_luna = round(perc_luna, 2)
      pixel_luna = (tot_pixel_luna * perc_luna) / 100 + 30
      pixel_luna =  round(pixel_luna)
      fase_luna = moon.phase(datetime.now())
      print("pixel luna -->", pixel_luna)
      print ("perc luna -->", perc_luna)
      
      '''
      #pixels.fill(OFF)
      for i in range(tot_pixel_luna):
            pixels[i+30] = CIELO_LUNA
            pixels.show()
      pixels.show()
      '''
   
   # Per la fase lunare
   # 0 .. 6.99 Luna Nuova
   # 7 .. 13.99 Primo Quarto
   # 14 .. 20.99 Luna Piena
   # 21 .. 27.99 Ultimo Quarto
      print ("fase luna -->", fase_luna)

   # PER DECIDERE LA SFUMATURA IN BASE ALLA FASE E ALLA POSIZIONE DELLA LUNA
      if (0<= fase_luna <= 6.99):
         print("Luna Nuova")
         pixels[pixel_luna] = (0, 0, 5)
         pixels[pixel_luna + 1] = (0, 0, 5)
         pixels.show()
         '''
         if (30<= pixel_luna <= 37):
            print("colore 1")
         if (38<= pixel_luna <= 45):
            print("colore 2")
         if (46<= pixel_luna <= 52):
            print("colore 3")
         if (53<= pixel_luna <= 0):
            print("colore 4")
         '''
      if (7<= fase_luna <= 13.99):
         print("Primo Quarto")
         pixels[pixel_luna] = (0, 0, 50)
         pixels[pixel_luna + 1] = (0, 0, 10)
         pixels.show()
         '''
         if (30<= pixel_luna <= 37):
            print("colore 1")
         if (38<= pixel_luna <= 45):
            print("colore 2")
         if (46<= pixel_luna <= 52):
            print("colore 3")
         if (53<= pixel_luna <= 0):
            print("colore 4")
         '''
      if (14<= fase_luna <= 20.99):
         print("Luna Piena")
         pixels[pixel_luna] = (0, 0, 100)
         pixels[pixel_luna + 1] = (0, 0, 100)
         pixels.show()
         '''
         if (30<= pixel_luna <= 37):
            print("colore 1")
         if (38<= pixel_luna <= 45):
            print("colore 2")
         if (46<= pixel_luna <= 52):
            print("colore 3")
         if (53<= pixel_luna <= 0):
            print("colore 4")
         '''
      if (21<= fase_luna <= 27.99):
         print("Ultimo Quarto")
         pixels[pixel_luna] = (10, 10, 50)
         pixels[pixel_luna - 1] = (0, 0, 25)
         pixels.show()
         '''
         if (30<= pixel_luna <= 37):
            print("colore 1")
         if (38<= pixel_luna <= 45):
            print("colore 2")
         if (46<= pixel_luna <= 52):
            print("colore 3")
         if (53<= pixel_luna <= 0):
            print("colore 4")
         '''
   time.sleep(150)
