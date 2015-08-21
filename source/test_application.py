import numpy
import cv2
from matplotlib import pyplot
from os.path import isfile, join
import pickle
import sys;

if len(sys.argv) != 3:
	# http://stackoverflow.com/questions/2949974/how-to-exit-a-program-sys-stderr-write-or-print
	sys.exit("Error: Num arguments should be 3. Actual arguments are "+len(sys.argv));


# Reading file names
input_file  = sys.argv[1]
output_file = sys.argv[2]
print input_file, output_file

# Reading input image
img = cv2.imread(input_file)
print img.shape
rows,cols,ch = img.shape


fig = pyplot.figure()
ax = fig.add_subplot(111)
ax.imshow(img, cmap = 'gray', interpolation = 'bicubic')

def onclick(event):
    print 'button=%d, x=%d, y=%d, xdata=%f, ydata=%f'%(
        event.button, event.x, event.y, event.xdata, event.ydata)

cid = fig.canvas.mpl_connect('button_press_event', onclick)


pyplot.xticks([]), pyplot.yticks([])  # to hide tick values on X and Y axis
pyplot.show()
