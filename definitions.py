class Agent():
    """
    Essa classe implementa a interface para o agente
    """

    def __init__(self, env):
        self.env = env

    def act(self):
        """
        Este método permite que o agente execue uma ação no ambiente
        """
        raise NotImplementedError('act')

class Environment:
    """
    Essa classe implementa a interface para o ambiente
    """

    def initial_percepts(self):
        """
        Este metodo retorna o estado do ambiente assim que o agente entra em contato com ele
        """
        raise NotImplementedError('initial_percepts')

    def signal(self,action):
        """
        Este metodo retorna o estado do ambiente depois de sofrer uma açao do agente
        """
        raise NotImplementedError('signal')