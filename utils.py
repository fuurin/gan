import tensorflow.compat.v1 as tf
from keras.backend import tensorflow_backend
from IPython.display import clear_output

def gpu_config():
    config = tf.ConfigProto(gpu_options=tf.GPUOptions(
        # visible_device_list="0", # specify GPU
        allow_growth=True
    ))
    session = tf.Session(config=config)
    tensorflow_backend.set_session(session)

class Outputter():
    def __init__(self, do=True):
        self.outputs = []
        self.do = do
    
    def save(self, filename):
        with open(filename, mode="w") as f:
            f.write("\n".join(self.outputs))
    
    def add(self, string):
        self.outputs.append(string)
        self.flush()
    
    def update(self, string):
        self.outputs[-1] = string
        self.flush()
    
    def conditional(self, string, condition):
        if condition:
            self.add(string)
        else:
            self.update(string)
    
    def flush(self):
        if not self.do: return
        clear_output()
        print("\n".join(self.outputs))
