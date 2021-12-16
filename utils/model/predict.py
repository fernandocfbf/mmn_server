from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog


def predict(img, predictor):
    '''
    input: predictor object (DefaultPredictor(cfg)), image to predict
    output: dictionary with all classes predicted (classes) and img with the model predictions
    description: predicts classes on the image using the predictor object
    '''
    outputs = predictor(img)
    v = Visualizer(img[:, :, ::-1], metadata=MetadataCatalog.get("train"), scale=1.2)
    out = v.draw_instance_predictions(outputs["instances"].to("cpu"))
    classes = outputs["instances"].pred_classes
    prediction = out.get_image()[:, :, ::-1]
    return {"classes": classes, "prediction": prediction}
