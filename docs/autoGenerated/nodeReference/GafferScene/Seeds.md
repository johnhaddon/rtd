# Seeds

Scatters points evenly over the surface of meshes.
This can be particularly useful in conjunction with
the Instancer, which can then apply instances to
each point.

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

## parent

 The location of the mesh to scatter the
points over. The generated points will
be parented under this location.

## name

 The name given to the object generated -
this will be placed under the parent in
the scene hierarchy.

## density

 The number of points per unit area of the mesh,
measured in object space.

## pointType

 The render type of the points. This defaults to
"gl:point" so that the points are rendered in a
lightweight manner in the viewport.

