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
        Este metodo retorna o estado do environment assim que o agente entra em contato com ele
        """
        raise NotImplementedError('initial_percepts')

    def signal(self,action):
        """
        Este metodo retorna o estado do environment depois de sofrer uma açao do agente
        """
        raise NotImplementedError('signal')