FROM python:3.11-slim

WORKDIR /opt/app

COPY . /opt/app

RUN apt update && \
    apt install -y libgl1-mesa-glx libglib2.0-0 libxkbcommon-x11-0 libxcb-xinerama0

RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["main.py"]