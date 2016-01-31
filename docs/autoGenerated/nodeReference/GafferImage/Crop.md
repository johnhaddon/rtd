# Crop

Modifies the Data and/or Display Window, in a way that is
either user-defined, or can be driven by the existing Data
or Display Window.

## user

 Container for user-defined plugs. Nodes
should never make their own plugs here,
so users are free to do as they wish.

## out

 The output image generated by this node.

## enabled

 Turns the node on and off.

## in

 The input image

## areaSource

 Where to source the actual area to use. If this is
set to DataWindow, it will use the input's Data Window,
if it is set to DisplayWindow, it will use the input's
Display Window, and if it is set to Custom, it will use
the Area plug.

## area

 The custom area to set the Data/Display Window to.
This plug is only used if 'Area Source' is set to
Custom.

## format

 The Format to use as the area to set the Data/Display
Window to. This plug is only used if 'Area Source' is
set to Format.

## formatCenter

 Whether to center the output image (based on the
existing display window) inside the new display
window format. This plug is only used if
'Area Source' is set to Format, and 'Affect Display
Window' it checked.

## affectDataWindow

 Whether to intersect the defined area with the input Data
Window. It will never pad black onto the Data Window, it
will only ever reduce the existing Data Window.

## affectDisplayWindow

 Whether to assign a new Display Window based on the defined
area.

## resetOrigin

 Shifts the cropped image area back to the origin, so that
the bottom left of the display window is at ( 0, 0 ).
