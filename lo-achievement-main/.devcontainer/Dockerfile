# Use the official image as a parent image.
FROM ubuntu:22.04

# Update the system
RUN apt-get -y update && apt-get install -y bash \
    build-essential \
    wget \
    make \
    git \
    curl \
    sudo \
    ca-certificates \
    poppler-utils \
    python3 \
    python3-pip \
    nodejs \
    npm && \
    rm -rf /var/lib/apt/lists/*

# Install python packages
RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    python3 -m pip install --no-cache-dir torch torchvision torchaudio && \
    python3 -m pip install --no-cache-dir \
    transformers \
    langchain \
    langchain[llms] \
    pypdf \
    tokenizers \
    sentencepiece \
    openai \
    librosa \
    datasets \
    jupyter \
    jupyterlab \
    pandas \
    openpyxl \
    matplotlib \
    numpy \
    seaborn \
    chromadb \
    tiktoken \
    unstructured \
    deeplake \
    ipyfilechooser \
    ipywidgets \
    widgetsnbextension \
    jupyter_contrib_nbextensions \
    jupyter_nbextensions_configurator \
    jupyterlab-git \
    gradio \
    streamlit \
    nb-clean \
    nbdime \
    nbdev

# Enable jupyter nbextension
# RUN jupyter nbextension enable --py widgetsnbextension

# Run nbdev_install_quarto
RUN sudo nbdev_install_quarto

# Indicate the Dockerfile owner
LABEL maintainer="Charreau Bell"

# Command to run on container start
CMD [ "/bin/bash" ]
