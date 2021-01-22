cd `dirname $0` && \
cd .. && \
sudo docker run \
  --ipc host \
  --gpus all \
  -ti \
  --rm \
  -u you \
  --mount type=bind,source="$(pwd)",target=/usr/src/app \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -e DISPLAY=unix$DISPLAY \
  --device=/dev/video0 \
  --name yolov5 \
  yolov5
