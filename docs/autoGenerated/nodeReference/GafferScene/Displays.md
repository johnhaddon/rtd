# Displays

Defines the image outputs to be created by the renderer. Arbitrary
outputs can be defined within the UI and also via the
`Outputs::addOutput()` API. Commonly used outputs may also
be predefined at startup via a config file - see
$GAFFER_ROOT/startup/gui/outputs.py for an example.

## user

 Container for user-defined plugs. Nodes
should never make their own plugs here,
so users are free to do as they wish.

## out

 The processed output scene.

## enabled

 The on/off state of the node. When it is off, the node outputs the input scene unchanged.

## in

 The input scene

## outputs

 The outputs defined by this node.

