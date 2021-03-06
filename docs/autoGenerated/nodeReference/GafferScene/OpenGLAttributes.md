# OpenGLAttributes

Applies attributes to modify the appearance of objects in
the viewport and in renders done by the OpenGLRender node.

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

## filter

 The filter used to control which parts of the scene are
processed. A Filter node should be connected here.

## attributes

 The attributes to be applied - arbitrary numbers of user defined
attributes may be added as children of this plug via the user
interface, or using the CompoundDataPlug API via python.

## attributes.primitiveSolid

 Whether or not the object is rendered solid, in which
case the assigned GLSL shader will be used to perform
the shading.

## attributes.primitiveWireframe

 Whether or not the object is rendered as a wireframe.
Use the primitiveWireframeColor and primitiveWireframeWidth
plugs for finer control of the wireframe appearance.

## attributes.primitiveWireframeColor

 The colour to use for the wireframe rendering. Only
meaningful if wireframe rendering is turned on.

## attributes.primitiveWireframeWidth

 The width in pixels of the wireframe rendering. Only
meaningful if wireframe rendering is turned on.

## attributes.primitiveOutline

 Whether or not an outline is drawn around the object.
Use the primitiveOutlineColor and primitiveOutlineWidth
plugs for finer control of the outline.

## attributes.primitiveOutlineColor

 The colour to use for the outline. Only
meaningful if outline rendering is turned on.

## attributes.primitiveOutlineWidth

 The width in pixels of the outline. Only
meaningful if outline rendering is turned on.

## attributes.primitivePoint

 Whether or not the individual points (vertices) of the
object are drawn. Use the primitivePointColor and primitivePointWidth
plugs for finer control of the point rendering.

## attributes.primitivePointColor

 The colour to use for the point rendering. Only
meaningful if point rendering is turned on.

## attributes.primitivePointWidth

 The width in pixels of the points. Only
meaningful if point rendering is turned on.

## attributes.primitiveBound

 Whether or not the bounding box of the object is drawn.
This is in addition to any drawing of unexpanded bounding
boxes that the viewer performs. Use the primitiveBoundColor
plug to change the colour of the bounding box.

## attributes.primitiveBoundColor

 The colour to use for the bounding box rendering. Only
meaningful if bounding box rendering is turned on.

## attributes.pointsPrimitiveUseGLPoints

 Points primitives have a render type (set by the PointsType
node) which allows them to be rendered as particles, disks,
spheres etc. This attribute overrides that type for OpenGL
only, allowing a much faster rendering as raw OpenGL points.

## attributes.pointsPrimitiveGLPointWidth

 The width in pixels of the GL points rendered when
the pointsPrimitiveUseGLPoints plug has overridden
the point type.

## attributes.curvesPrimitiveUseGLLines

 Curves primitives are typically rendered as ribbons
and as such have an associated width in object space.
This attribute overrides that for OpenGL only, allowing
a much faster rendering as raw OpenGL lines.

## attributes.curvesPrimitiveGLLineWidth

 The width in pixels of the GL lines rendered when
the curvesPrimitiveUseGLLines plug has overridden
the drawing to use lines.

## attributes.curvesPrimitiveIgnoreBasis

 Turns off interpolation for cubic curves, just
rendering straight lines between the vertices
instead.

## global

 Causes the attributes to be applied to the scene globals
instead of the individual locations defined by the filter.

