from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog
import cv2

from utils.model.image_show import image_show
from constants import *


def predict(img, predictor, test=False):
    '''
    input: predictor object (DefaultPredictor(cfg)), image to predict (array)
    output: dictionary with all classes predicted (classes) and img with the model predictions
    description: predicts classes on the image using the predictor object
    '''
    thing_classes = ['food-images', 'french_fries', 'hot_dog', 'rice', 'salad', 'steak']
    MetadataCatalog.get("train").set(thing_classes=thing_classes)

    if test:
        img_test = cv2.imread(MODEL_IMG_TEST)
        outputs = predictor(img_test)
        v = Visualizer(img_test[:, :, ::-1], metadata=MetadataCatalog.get("train"), scale=1.2)
    else:
        outputs = predictor(img)
        v = Visualizer(img[:, :, ::-1], metadata=MetadataCatalog.get("train"), scale=1.2)

    out = v.draw_instance_predictions(outputs["instances"].to("cpu"))
    classes = outputs["instances"].pred_classes
    prediction = cv2.resize(out.get_image()[:, :, ::-1], (100, 100))
    
    return {"classes": classes, "prediction": prediction.tolist()}
