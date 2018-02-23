

#GUI Test - TKinter (TK-interface)

from tkinter import *
from tkinter import filedialog
#import cv2
#import NumPy as np

#PLANNING:
#Buttons: call function -> make function to invoke stitcher test for now
#	Pass contents of a text box/get file location to Pass
	#path = tkFileDialog.askopenfilename()
	#btn = Button(root, text="Select an image", command=select_image)
		#command = fxn call

#https://www.pyimagesearch.com/2016/05/23/opencv-with-tkinter/
	#Idea: Shows images side by side -> go through each file uploaded (slideshow),
	# have user approve key points for each

def selectImage():
	#Open a prompt for the user to select a directoy holding the files
	path = filedialog.askdirectory()

	if len(path) > 0:	#User didn't press cancel
		print("Got path: " + path)
		#TODO open stitcher test or w/e, passing
		#Use os.system("script.py path")
		#ALT: execfile("script.py path") - runs in same context



#Initialize
root = Tk()

#panelOrig = None #L/R panels displaying images in; original and new
#panelNew = None		#Left in for comparing images idea


#Create button to open image directory selection dialog
btn = Button(root, text = "Open an Image Directory", command = selectImage)
btn.pack(side = "bottom", fill = "both", expand = "yes", padx = "10", pady = "10")


#Start GUI
root.mainloop()















