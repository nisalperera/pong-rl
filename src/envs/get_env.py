import gymnasium
import ale_py

gymnasium.register_envs(ale_py)


def get_env(env_name="ALE/Pong-v5"):
    return gymnasium.make(env_name)

