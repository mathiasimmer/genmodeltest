
class IContainer(object):
    pass
    # Start of user code -> properties/constructors for IContainer class(interface)

    # End of user code
    def2 create(self):
        # Start of user code protected zone for create function body
        raise NotImplementedError
        # End of user code	
    def2 start(self):
        # Start of user code protected zone for start function body
        raise NotImplementedError
        # End of user code	
    # Start of user code -> methods for IContainer class(interface)

    # End of user code

class Service(object):
    def __init__(self):
        
        self.containers = []
        
    # Start of user code -> properties/constructors for Service class

    # End of user code
    # Start of user code -> methods for Service class

    # End of user code

class DockerContainer(IContainer):
    pass
    # Start of user code -> properties/constructors for DockerContainer class

    # End of user code
    # Start of user code -> methods for DockerContainer class

    # End of user code


# Start of user code -> functions/methods for model package

# End of user code
