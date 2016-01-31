# PythonCommand

Runs python code.

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

## command 

 The command to run. This may reference any of the
variables by name, and also the node itself as `self`
and the current context as `context`. 

## variables 

 An arbitrary set of variables which can be accessed via
the `variables` dictionary within the python command. 

## sequence 

 Calls the command once for each sequence, instead of once
per frame. In this mode, an additional variable called `frames`
is available to the command, containing a list of all frame
numbers for which execution should be performed. The context may
be updated to reference any frame from this list, and accessing
a variable returns the value for the current frame.

A typical structure for the command might look something like this :

```
# Do some one-time initialization
...
# Process all frames
for frame in frames :
        context.setFrame( frame )
        # Read variables after setting the frame to get
        # the right values for that frame.
        v = variables["v"]
        ...
# Do some one-time finalization
...
``` 
