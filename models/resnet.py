from tensorflow.keras.applications import ResNet50

def build_resnet(input_shape, num_classes):
    model = ResNet50(weights=None, input_shape=input_shape, classes=num_classes)
    return model
