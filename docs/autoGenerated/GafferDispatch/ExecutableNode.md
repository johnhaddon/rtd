# ExecutableNode

Base class for nodes which have external side effects - generating
files on disk for instance. Can be connected with other executable
nodes to define an order of execution based on dependencies between
nodes. A Dispatcher can then be used to actually perform the execution
of such a network.

