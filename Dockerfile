FROM python:3.7.4

WORKDIR /workspaces/python_init

RUN pip install pytest hypothesis
