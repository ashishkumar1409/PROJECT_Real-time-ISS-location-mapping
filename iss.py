import reverse_geocoder as rg
def reverseGeocode(coordinates):
  result = rg.search(coordinates)
  return list(result[0].items())
coordinates =(28.613939, 77.209023)
a = reverseGeocode(coordinates)
print(a[2][1])
print("\n")
import json
import urllib.request
import turtle
import time
global lat
global lon
lat = 0
lon = 0
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print('People in Space: ', result['number'])
people = result['people']
for p in people:
  print(p['name'], ' in ', p['craft'])
def updateloc():
  url = 'http://api.open-notify.org/iss-now.json'
  response = urllib.request.urlopen(url)
  result = json.loads(response.read())
  location = result['iss_position']
  lat = 2*float(location['latitude'])
  lon = 2*float(location['longitude'])
  iss.goto(lon, lat)
  print(lon,lat)
  return [lon,lat]
screen = turtle.Screen()
screen.setup(1440,720)
screen.setworldcoordinates(-360, -180, 360, 180)
screen.register_shape('iss.gif')
screen.bgpic('map.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)
iss.penup()
updateloc()
x = 0
y = 0
writeloc = turtle.Turtle()
writeloc.penup()
writeloc.color('white')
writeloc.hideturtle()
def get_mouse_click_coor(x, y):
  list = updateloc()
  lat = list[1]
  lon = list[0]
  if (x > lon - 5 and x < lon + 5 and y > lat - 5 and y < lat+5):
    print(x,y)
    writeloc.goto(x,y)
    a = reverseGeocode((lat/2,lon/2))
    writeloc.write("Longitude : "+str(lon) + "\nLatitude : " + str(lat)+"\nPlace : "+ a[2][1],font=("Arial", 20, 'normal', 'bold'))
    time.sleep(5)
    writeloc.clear()
  else:
    print(x,y)
    writeloc.goto(x,y)
    a = reverseGeocode((y/2,x/2))
    writeloc.write("Longitude : "+str(x) + "\nLatitude : " + str(y)+"\nPlace : "+ a[2][1],font=("Arial", 20, 'normal', 'bold'))
    time.sleep(3)
    writeloc.clear()
print(x,y)
while(True):
  updateloc()
  turtle.onscreenclick(get_mouse_click_coor)
screen.mainloop()
