# SetFilter

A filter which uses sets to define which locations are matched.

## user

 Container for user-defined plugs. Nodes
should never make their own plugs here,
so users are free to do as they wish.

## enabled

 The on/off state of the filter. When it is off, the
filter does not match any locations.

## out

 The result of the filter. This should be connected into
the "filter" plug of a FilteredSceneProcessor.

## set

 The name of a set that defines the locations to
be matched.

