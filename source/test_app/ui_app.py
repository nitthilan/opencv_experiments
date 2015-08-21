import numpy
import cv2
from matplotlib import pyplot
from matplotlib.widgets import Button, Slider
import sys

sys.path.append("../library/")

import image_correction as ic

if len(sys.argv) != 2:
	# http://stackoverflow.com/questions/2949974/how-to-exit-a-program-sys-stderr-write-or-print
	sys.exit("Error: Num arguments should be 2. Actual arguments are "+len(sys.argv));

# Reading file names
input_file  = sys.argv[1]
# Reading input image
img = cv2.imread(input_file)
print img.shape
rows,cols,ch = img.shape

threshold = 200
radius = 3

output = ic.InvDiffOfGaussian(img, radius, threshold)

# Start the ui loop
fig = pyplot.figure()
ax = fig.add_subplot(111)
fig1 = ax.imshow(output, cmap = 'gray', interpolation = 'bicubic')

# def onclick(event):
#     print 'button=%d, x=%d, y=%d, xdata=%f, ydata=%f'%(
#         event.button, event.x, event.y, event.xdata, event.ydata)
# cid = fig.canvas.mpl_connect('button_press_event', onclick)

# Updating threshold and radius
axcolor = 'lightgoldenrodyellow'
axthreshold = pyplot.axes([0.12, 0.04, 0.65, 0.03], axisbg=axcolor)
sthreshold = Slider(axthreshold, 'Threshold', 100, 255, valinit=threshold)
axradius = pyplot.axes([0.12, 0.01, 0.65, 0.03], axisbg=axcolor)
sradius = Slider(axradius, 'Radius', 1, 10, valinit=radius)
def update(val):
    radius = sradius.val
    threshold = sthreshold.val
    output = ic.InvDiffOfGaussian(img, radius, threshold)
    #fig1.draw()
    ax.imshow(output, cmap = 'gray', interpolation = 'bicubic')
    fig.canvas.draw_idle()
    #print (sthreshold.val, sradius.val, radius, threshold)
    
sthreshold.on_changed(update)
sradius.on_changed(update)


# Do the actual processing
def on_button_press(event):
	print (radius, threshold)
	output = ic.InvDiffOfGaussian(img, radius, threshold)
	ax.imshow(output, cmap = 'gray', interpolation = 'bicubic')
	#print event
process = pyplot.axes([0.01, 0.01, 0.1, 0.075])
bprocess = Button(process, 'Process')
bprocess.on_clicked(on_button_press)

pyplot.xticks([]), pyplot.yticks([])  # to hide tick values on X and Y axis
pyplot.show()



