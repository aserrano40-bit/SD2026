#buscar en dockerHub si existe un distro de linux especifico 
#0 busca una ambiente para el docker 
From ubuntu:latest

#argumenta al sistema operativo para que el GUI no cause problemas 
ARG DEBIAN_FRONTEND=noninteractive

#se instala Python 
#apt update
RUN apt-get update &&\
apt-get install -y \
Python3 Python3-pip \
git curl && \
ra -rf /var/lib/apt/lists/*


WORKDIR /workspace


RUN git clone https://github.com/aserrano40-bit/SD2026.git

CMD ["sleep", "infinity"]
#CMD [/bin/bash]
#CMD ["python3", "RCDD_2026/main.py"]