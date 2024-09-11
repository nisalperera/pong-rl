from tensorflow.keras.optimizers import Adam


def get_optimizer(lr=0.0001):
    return Adam(learning_rate=lr)