from detectron2.config import get_cfg
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor

from constants import *


def prepare_rcnn_model():
    '''
    input: empty
    output: returns the predictor object
    description: prepare the model using the pre-trained weights
    '''
    cfg = get_cfg()
    cfg.merge_from_file(model_zoo.get_config_file(MODEL_CONFIG_FILE))
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = MODEL_THRESHOLD
    cfg.MODEL.WEIGHTS = MODEL_WEIGHTS
    cfg.MODEL.ROI_HEADS.NUM_CLASSES = MODEL_NUM_CLASSES
    return DefaultPredictor(cfg)
