FROM tensorflow/tensorflow:2.13.0-gpu

RUN pip3 install swig

COPY ./requirements.txt ./

RUN pip3 install -r requirements.txt "gymnasium[accept-rom-license]"
# RUN pip3 install tensorflow-rl keras-rl gymnasium[atari] "gymnasium[accept-rom-license]"
