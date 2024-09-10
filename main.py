import gymnasium
import ale_py

gymnasium.register_envs(ale_py)

gymnasium.make("ALE/Pong-v5")

