import cv2

def load_model():
    net = cv2.dnn.readNetFromTensorflow("models/frozen_inference_graph.pb", "models/pipeline.config")
    return net
