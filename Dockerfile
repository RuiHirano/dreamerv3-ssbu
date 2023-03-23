FROM --platform=linux/x86_64 tensorflow/tensorflow:2.11.0-gpu

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get -y install \
    git \
    vim \
    libgl1-mesa-dev \
    cmake libz-dev \
    ffmpeg \
    libcudnn8=8.4.1.50-1+cuda11.6 \
    && rm -rf /var/lib/apt/lists/*

# libgl1-mesa-dev for opencv
# cmake libz-dev for gym[atari]

# install libultimate
RUN pip install git+https://github.com/DeepSmashProject/libultimate.git@1.2.1

WORKDIR /dreamerv3-ssbu
COPY requirements.txt .
RUN pip --no-cache-dir install -r requirements.txt

COPY . .

CMD [ "bash" ]