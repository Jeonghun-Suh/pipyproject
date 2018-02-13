#from cs1graphics import *
from cs1media import *

img = load_picture('/home/jsuh/Software/Maps/Map.png')
file1 = open('/home/clients/display/dangerlevels', 'r')
lst = file1.readlines()
last_line = lst[-1].split(',')
w, h = img.size()

#canvas = Canvas(w, h)
#canvas.setTitle("Displaying Part")

#pre-defined range: [[x_min, x_max],[y_min, y_max]]
pi01_range = [[30,100], [130,250]]

def image_process(image, line):
	for y in range(h):
		for x in range(w):
			r, g, b = image.get(x,y)

			if pi01_range[0][0] < x < pi01_range[0][1]:
				if pi01_range[1][0] < y < pi01_range[1][1]:
					r = int(r*(1.0+1.0*float(line[-1])))
					g = int(g - 500.0*float(line[-1]))
					b = int(b - 500.0*float(line[-1]))
					if r>255: r = 255
					if g>255: g = 255
					if b>255: b = 255
					if g<0: g = 0
					if b<0: b = 0
					image.set(x,y,(r,g,b))
image_process(img, last_line)

img.save_as("/var/www/html/Map_updated.jpg")
img.show()
#canvas.wait()
