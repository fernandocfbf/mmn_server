MODEL_CONFIG_FILE = "COCO-Detection/faster_rcnn_R_101_FPN_3x.yaml" #model file
MODEL_THRESHOLD = 0.5 #define model threshold
MODEL_WEIGHTS = "./model_final.pth" #path to model weights
MODEL_NUM_CLASSES = 6 #num of classes into the model
MODEL_IMG_TEST = "./test/mix.png" #random test image
MODEL_THING_CLASSES = ['food-images', 'french_fries', 'hot_dog', 'rice', 'salad', 'steak'] #available classes
