# FilterSwitch

Chooses between multiple input filters, passing the chosen
filter through to the output.

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

## in

 The input filters

## index

 The index of the input which is passed through. A value
of 0 chooses the first input, 1 the second and so on. Values
larger than the number of available inputs wrap back around to
the beginning.

