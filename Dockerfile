FROM pytorch/pytorch:2.4.1-cuda12.1-cudnn9-devel

COPY ./requirements-gpu.txt /opt/program/requirements-gpu.txt

WORKDIR /opt/program/

RUN pip install -r requirements-gpu.txt
