from constants import *

def class_to_string(object):
    text = str(object)
    text_filter = text.replace(", device='cuda:0')", "").replace("tensor(", "")
    class_list = text_filter.strip('][').split(', ')
    res = list()
    for value in class_list:
        res.append(MODEL_THING_CLASSES[int(value)])
    return res