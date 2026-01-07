# learn_ray

run in docker

- docker pull rayproject/ray:latest-cpu
- docker run -it --shm-size=2g -p 8265:8265 -p 6379:6379 rayproject/ray:latest-cpu bash -c "ray start --head --dashboard-host=0.0.0.0 --block"
