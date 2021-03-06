# InteractiveRenderManRender

Performs interactive renders using a RenderMan renderer
which supports interactive edits. In 3delight the following
edits are currently supported :

- Adding/removing lights
- Adjusting light parameters
- Moving the camera
- Moving coordinate systems
- Changing shader assignments
- Editing shader networks
- Editing shader parameters

## user

 Container for user-defined plugs. Nodes
should never make their own plugs here,
so users are free to do as they wish.

## in

 The scene to be rendered.

## out

 A direct pass-through of the input scene.

## state

 The interactive state.

## updateLights

 When on, changes to lights are reflected in the
interactive render.

## updateAttributes

 When on, changes to attribute (and shaders) are reflected in the
interactive render. When working with complex scenes, it may be
worth turning this off to gain increased performance when only
editing lights.

## updateCameras

 When on, changes to the camera are reflected in the
interactive render.

## updateCoordinateSystems

 When on, changes to coordinate systems are reflected in the
interactive render.

