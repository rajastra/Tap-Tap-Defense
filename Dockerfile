FROM ubuntu

MAINTAINER Eder Santana <edercsjr@gmail.com>

RUN apt-get update && apt-get install -y \
    mercurial \
    libav-tools \
    libsdl-image1.2-dev \
    libsdl-mixer1.2-dev \
    libsdl-ttf2.0-dev \
    libsmpeg-dev \
    libsdl1.2-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    libplib-dev \
    libopenal-dev \
    libalut-dev \
    libvorbis-dev \
    libxxf86vm-dev \
    libxmu-dev \
    libgl1-mesa-dev \
    python-dev \
    python-pip \
    python-numpy \
    python-scipy \
    python-pygame \
    git

# RUN hg clone https://bitbucket.org/pygame/pygame && cd pygame && python setup.py build && sudo python setup.py install && cd ..
RUN pip install keras git+https://github.com/ntasfi/PyGame-Learning-Environment.git
RUN git clone https://github.com/ntasfi/PyGame-Learning-Environment.git ple