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
    
    # Get the directory where the results are saved
    for result in results:
        save_dir = result.save_dir
        break  # since there's only one result, we can break after finding it

    # Initialize the path to the jpg image
    image_path = None
    
    # Traverse the save_dir and find the single JPG image
    for root, dirs, files in os.walk(save_dir):
        for file in files:
            if file.lower().endswith('.jpg'):
                image_path = os.path.join(root, file)
                break  # since there's only one image, we can break after finding it
        if image_path:
            break
    
    # Read and encode the image to base64
    if image_path:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            img_tag = f'<img src="data:image/jpeg;base64,{encoded_string}"/>'
    else:
        img_tag = '<p>No image found</p>'
    
    #return {"body": f"<html><body>{img_tag}</body></html>"}
    return {"body": str(encoded_string)}