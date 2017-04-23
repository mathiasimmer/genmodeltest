from abc import abstractmethod
class Service(object):
    def __initmodel__(self):
        self.name = ""
        self.__orchestration = None
        
        self.containers = []
        
    # Start of user code -> properties/constructors for Service class
        self.orchestration = None
    # End of user code
    
    
    def __init__(self, orchestration):
        # Start of user code protected zone for __init__ function body
        self.__initmodel__()

        # End of user code	
    # Start of user code -> methods for Service class

        # End of user code

class IOrchestration(object):
    pass
    # Start of user code -> properties/constructors for IOrchestration class(interface)

    # End of user code
    # Start of user code -> methods for IOrchestration class(interface)

    # End of user code

class Component(object):
    pass
    # Start of user code -> properties/constructors for Component class

    # End of user code
    # Start of user code -> methods for Component class

    # End of user code

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



class Deros(object):
    pass
    # Start of user code -> properties/constructors for Deros class

    # End of user code
    
    
    def start(self, component):
        # Start of user code protected zone for start function body
        raise NotImplementedError
        # End of user code	
    
    
    def stop(self, component):
        # Start of user code protected zone for stop function body
        raise NotImplementedError
        # End of user code	
    # Start of user code -> methods for Deros class

        # End of user code

class DockerOrchestration(IOrchestration):
    pass
    # Start of user code -> properties/constructors for DockerOrchestration class

    # End of user code
    # Start of user code -> methods for DockerOrchestration class

    # End of user code

class DockerContainer(IContainer):
    pass
    # Start of user code -> properties/constructors for DockerContainer class

    # End of user code
    # Start of user code -> methods for DockerContainer class

    # End of user code

class Leaf(Component):
    pass
    # Start of user code -> properties/constructors for Leaf class

    # End of user code
    # Start of user code -> methods for Leaf class

    # End of user code

class Composite(Component):
    def __initmodel__(self):
        
        self.components = []
        
    # Start of user code -> properties/constructors for Composite class

        # End of user code
    # Start of user code -> methods for Composite class

        # End of user code


# Start of user code -> functions/methods for model package

# End of user code
