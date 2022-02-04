from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog
import cv2
import base64

from utils.model.image_show import image_show
from utils.model.tranform_classes import class_to_string
from constants import *

from PIL import Image



def predict(img, predictor, test=False):
    '''
    input: image to predict (array), predictor object (DefaultPredictor(cfg)) and test flag (boolean)
    output: dictionary with all classes predicted (classes) and img with the model predictions
    description: predicts classes on the image using the predictor object
    '''
    MetadataCatalog.get("train").set(thing_classes=MODEL_THING_CLASSES)

    if test:
        img_test = cv2.imread(MODEL_IMG_TEST)
        outputs = predictor(img_test)
        v = Visualizer(img_test[:, :, ::-1], metadata=MetadataCatalog.get("train"), scale=1.2)
    else:
        outputs = predictor(img)
        v = Visualizer(img[:, :, ::-1], metadata=MetadataCatalog.get("train"), scale=1.2)

    out = v.draw_instance_predictions(outputs["instances"].to("cpu"))
    classes = outputs["instances"].pred_classes
    prediction = cv2.resize(out.get_image()[:, :, ::-1], (400, 400))
    cv2.imwrite('prediction_test.jpg', prediction)
    classes_tranform = class_to_string(classes)
    return classes_tranform, prediction
