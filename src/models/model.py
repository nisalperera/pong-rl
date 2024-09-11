from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Flatten, Convolution2D, Permute


def build_model(input_shape, nb_actions):
    model = Sequential()
    
    model.add(Permute(2, 3, 1), input_shape=input_shape)
    
    model.add(Convolution2D(32, (8, 8), strides=(4, 4), kernel_initializer="he_normal"))
    model.add(Activation("relu"))
    model.add(Convolution2D(32, (4, 4), strides=(2, 2), kernel_initializer="he_normal"))
    model.add(Activation("relu"))
    model.add(Convolution2D(32, (2, 2), strides=(1, 1), kernel_initializer="he_normal"))
    model.add(Activation("relu"))
    
    model.add(Flatten())
    
    model.add(Dense(512))
    model.add(Activation("relu"))
    model.add(Dense(1024))
    model.add(Activation("relu"))
    
    model.add(Dense(nb_actions))
    model.add(Activation("linear"))
    
    return model

def load_weights(input_shape, nb_actions, weights=None):
    
    model = build_model(input_shape, nb_actions)
    try:
        model = model.load_weights(weights)
        return model, True
    except:
        return model, False