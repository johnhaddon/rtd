# ShaderSwitch

Chooses between multiple input shaders, passing through the
chosen shader to the output. The switching is resolved
before rendering begins, so no per-sample overhead is
incurred during shading.

## user

 Container for user-defined plugs. Nodes
should never make their own plugs here,
so users are free to do as they wish.

## index

 The index of the input which is passed through. A value
of 0 chooses the first input, 1 the second and so on. Values
larger than the number of available inputs wrap back around to
the beginning.

## enabled

 Turns the node on and off.

## in

 The input shaders - the index plug decides
which of these is passed through to the output.

## out

 The output shader.

