from rl.policy import LinearAnnealedPolicy, EpsGreedyQPolicy

def get_policy(attr="eps", value_max=1, value_min=0.1, value_test=0.05, nb_steps=500000):
    return LinearAnnealedPolicy(EpsGreedyQPolicy(), 
                                    attr=attr, 
                                    value_max=value_max,
                                    value_min=value_min,
                                    value_test=value_test,
                                    nb_steps=nb_steps
                                )