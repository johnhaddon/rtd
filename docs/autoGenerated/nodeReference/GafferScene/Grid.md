# Grid

"
A grid. This is used to draw the grid in the viewer,
but is also included as a node in case it might be
useful, perhaps for placing a grid in renders done
using the OpenGLRender node.

## user

 Container for user-defined plugs. Nodes
should never make their own plugs here,
so users are free to do as they wish.

## out

 The output scene.

## enabled

 The on/off state of the node. When it is off, the node outputs
an empty scene.

## name

 The name of the grid.

## transform

 The transform applied to the grid.

## dimensions

 The size of the grid in the x and y
axes. Use the transform to rotate the
grid into a different plane.

## spacing

 The size of the space between adjacent lines
in the grid.

## gridColor

 The colour of the lines forming the main part
of the grid.

## centerColor

 The colour of the two lines forming the central
cross of the grid.

## borderColor

 The colour of the lines forming the border
of the grid.

## gridPixelWidth

 The width of the lines forming the main part
of the grid. This width applies only to the
OpenGL representation of the grid.

## centerPixelWidth

 The width of the two lines forming the central
cross of the grid. This width applies only to the
OpenGL representation of the grid.

## borderPixelWidth

 The width of the lines forming the border
of the grid. This width applies only to the
OpenGL representation of the grid.

