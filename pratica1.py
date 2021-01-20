class Agent():
    """
    """
    def __init__(self, env):
        self.env = env

    def act(self):
        raise NotImplementedError('act')

class Environment:
    
    def initial_percepts(self):
        """
        Este metodo retorna o estado do environment
        """
        raise NotImplementedError('initial_percepts')

    def signal(self,action):
        raise NotImplementedError('signal')