from abc import abstractmethod
class IContainer(object):
    pass
    # Start of user code -> properties/constructors for IContainer class(interface)

    # End of user code
    @abstractmethod
    def create(self):
        # Start of user code protected zone for create function body
        raise NotImplementedError
        # End of user code	
    @abstractmethod
    def start(self):
        # Start of user code protected zone for start function body
        raise NotImplementedError
        # End of user code	
    @abstractmethod
    def run(self):
        # Start of user code protected zone for run function body
        raise NotImplementedError
        # End of user code	
    @abstractmethod
    def remove(self):
        # Start of user code protected zone for remove function body
        raise NotImplementedError
        # End of user code	
    # Start of user code -> methods for IContainer class(interface)

    # End of user code

