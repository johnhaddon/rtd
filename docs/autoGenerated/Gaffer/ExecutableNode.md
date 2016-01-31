# ExecutableNode

Base class for nodes which have external side effects - generating
files on disk for instance. Can be connected with other executable
nodes to define an order of execution based on dependencies between
nodes. A Dispatcher can then be used to actually perform the execution
of such a network.

## user 

 Container for user-defined plugs. Nodes
should never make their own plugs here,
so users are free to do as they wish. 

## preTasks 

 Input connections to upstream nodes which must be
executed before this node. 

## postTasks 

 Input connections to nodes which must be
executed after this node, but which don't
need to be executed before downstream nodes. 

## task 

 Output connections to downstream nodes which must
not be executed until after this node. 

## dispatcher 

 Container for custom plugs which dispatchers use to
control their behaviour. 

