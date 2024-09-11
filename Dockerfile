FROM tensorflow/tensorflow:2.14.0-gpu

RUN pip3 install swig

RUN pip3 install tensorflow-rl gymnasium[atari] "gymnasium[accept-rom-license]"
