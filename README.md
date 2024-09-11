# pog-rl
Use Reinforcement Learning to learn how to play Pong


docker run -id --rm --ipc=host --gpus all -v "$PWD"/src/:/opt/program/ --name tensorflow-rl rl:1

docker run -id --rm -u $(id -u):$(id -g) --ipc=host --gpus all -v "$PWD"/src/:/opt/program/ --name tensorflow-rl rl:1