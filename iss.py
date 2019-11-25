import reverse_geocoder as rg
import json
import urllib.request
import turtle
import time


global lat
global lon



url = 'http://api.open-notify.org/astros.json'  # source providing api for getting live location data
response = urllib.request.urlopen(url)  # storing response of server in response vatiable
result = json.loads(response.read()) # reading resonse and storing it in result  ( json used as response is in json format)


url2 = 'http://api.open-notify.org/iss-now.json'
response2 = urllib.request.urlopen(url2)
result2 = json.loads(response2.read())
location = result2['iss_position']

lat = 2 * float(location['latitude'])  # multiplying by 2 as we have doubled the original size of nasa image and turtle screen so
# latitude and longitude means cordinate must also be multiplied by 2
lon = 2 * float(location['longitude'])

#function for getting place name from latitude,longitude

def reverseGeocode(coordinates):
  result = rg.search(coordinates)
  return list(result[0].items())

# printing number of people and name of each in space reading from response of api
print('People in Space: ', result['number'])
people = result['people']
for p in people:
  print(p['name'], ' in ', p['craft'])

#function to update location of iss and moving iss object to updated location
def updateloc():
  url = 'http://api.open-notify.org/iss-now.json'
  response = urllib.request.urlopen(url)
  result = json.loads(response.read())
  location = result['iss_position']
  lat = 2*float(location['latitude'])  #multiplying by 2 as we have doubled the original size of nasa image and turtle screen so
                                        #latitude and longitude means cordinate must also be multiplied by 2
  lon = 2*float(location['longitude'])

#code to stop drawing trajectory when iss goes from one end to another

  #to check if iss is at the end of screen and if it is use pendown() so that it stop drawing trajectory
  if  iss.pos()[0]-lon > 710 or iss.pos()[1]-lat > 360 or iss.pos()[1]-lat < -360 or iss.pos()[0]-lon < -710 :
    iss.penup()
    iss.goto(lon,lat)
    iss.pendown()
  else:
    iss.goto(lon,lat)
    iss.pendown()


  print(lon,lat)
  return [lon,lat]
screen = turtle.Screen()
screen.setup(1440,720)
screen.setworldcoordinates(-360, -180, 360, 180)
screen.register_shape('iss.gif')
screen.bgpic('map.gif')


iss = turtle.Turtle()
iss.hideturtle()
#iss.speed(10000)
iss.shape('iss.gif')
iss.setheading(90)
iss.penup()
iss.color("Yellow")
updateloc()
iss.showturtle()

x = 0
y = 0
writeloc = turtle.Turtle()
writeloc.penup()
writeloc.color('white')
writeloc.hideturtle()

d = reverseGeocode((lat/2, lon/2))
writeloc.goto(lon,lat)
writeloc.write("Longitude : " + str(lon) + "\nLatitude : " + str(lat) + "\nPlace : " + d[2][1],font=("Arial", 20, 'normal', 'bold'))
time.sleep(3)
writeloc.clear()
'''
def drag_handler(x, y):
  iss.ondrag(None) # disable event inside event handler
  iss.penup()
  iss.goto(x, y)

  iss.ondrag(drag_handler)
'''

def get_mouse_click_coor(x, y):
  list = updateloc()
  lat = list[1]
  lon = list[0]
  if (x > lon - 5 and x < lon + 5 and y > lat - 5 and y < lat+5):
    print(x,y)
    writeloc.goto(x,y)
    a = reverseGeocode((lat/2,lon/2))
    writeloc.write("Longitude : "+str(lon) + "\nLatitude : " + str(lat)+"\nPlace : "+ a[2][1],font=("Arial", 20, 'normal', 'bold'))
    time.sleep(3)
    writeloc.clear()
  else:
    print(x,y)
    writeloc.goto(x,y)
    a = reverseGeocode((y/2,x/2))
    writeloc.write("Longitude : "+str(x) + "\nLatitude : " + str(y)+"\nPlace : "+ a[2][1],font=("Arial", 20, 'normal', 'bold'))
    time.sleep(3)
    writeloc.clear()
print(x,y)


'''CODE FOR REAL TIME UPDATE TILL INFINITY'''
while(True):
  updateloc()
  turtle.onscreenclick(get_mouse_click_coor)


screen.mainloop()