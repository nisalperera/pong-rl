FROM pytorch/pytorch:2.4.1-cuda12.1-cudnn9-devel

COPY ./requirements-gpu.txt /opt/program/requirements-gpu.txt

WORKDIR /opt/program/

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    software-properties-common && \
    rm -rf /var/lib/apt/lists/*

RUN add-apt-repository ppa:deadsnakes/ppa -y

RUN apt update && apt install -y --no-install-recommends \
    git \
    python3.10 \ 
    python3.10-dev \ 
    python3-pip \ 
    libffi-dev \
    cmake\
    gcc\
    g++\
    gfortran\
    ninja-build \
    pkg-config \
    ffmpeg \
    x264 \
    libx264-dev \
    libavcodec-dev \
    libavformat-dev \
    libxvidcore-dev \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libjpeg-turbo8-dev \
    libwebp-dev \
    libtiff5-dev \
    libopenjp2-7-dev \
    libv4l-dev\
    libswscale-dev\
    libgtk-3-dev\
    zlib1g-dev \
    unzip \
    libfreetype6-dev \
    libfribidi-dev \
    libharfbuzz-dev \
    libraqm0 \
    openexr \
    libatlas-base-dev\
    libtbb2 \
    libtbb-dev \
    openssh-client \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN python3.10 -m pip install -r requirements-gpu.txt