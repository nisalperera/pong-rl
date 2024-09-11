from rl.agents import DQNAgent

def get_agent(
        model, 
        **kwargs
    ):
    return DQNAgent(model, **kwargs)