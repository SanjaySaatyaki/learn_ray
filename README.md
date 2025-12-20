# learn_ray

run in docker

- docker pull rayproject/ray:latest-cpu
- docker run -it --shm-size=2g -p 8265:8265 -p 8000:8000 rayproject/ray:latest-cpu bash