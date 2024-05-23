#from ultralytics import YOLO
#def main(args):
    #msg = 'you did not tell me who you are.'
    #if 'name' in args:
    #    name = args['name']
    #    msg = f"hello {name} python!"
    #return {"body": f"<html><body><h3>{msg}</h3></body></html>"}
#	model = YOLO('yolov8n.pt')  # load an official model
#	path = ""
	# Predict with the model
#	results = model('https://ultralytics.com/images/bus.jpg', save=True)  # predict on an image
#	for result in results:
#		path = result.save_dir
#	return {"body": f"<html><body><h3>{path}</h3></body></html>"}

from ultralytics import YOLO
import os
import base64

def main(args):
    model = YOLO('yolov8n.pt')  # load an official model
    # Predict with the model and save the results
    results = model('https://ultralytics.com/images/bus.jpg', save=True)
    save_dir =""    
    # Get the directory where the results are saved
    for result in results:
        save_dir = result.save_dir

    
    #return {"body": f"<html><body>{img_tag}</body></html>"}
    return {"body": str(save_dir)}