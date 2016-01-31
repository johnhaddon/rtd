# Text

Renders text over an input image.

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

## color

 The colour of the text.

## shadow

 Enables the rendering of a drop shadow which can be coloured, offset and
blurred.

## shadowColor

 The colour of the shadow.

## shadowOffset

 The offset of the shadow, measured in pixels.

## shadowBlur

 A blur applied to the shadow, measured in pixels.

## text

 The text to be rendered.

## font

 The font to render the text with. This should be a .ttf font file which
is located on the paths specified by the IECORE_FONT_PATHS
environment variable.

## size

 The size of the font in pixels. For best quality results
for constant sized text prefer this over the scale setting
on the transform, which is better suited for smoothly animating
the size.

## area

 The area of the image within which the text is rendered.
The text will be word wrapped to fit within the area and
justified as specified by the justification setting. If the
area is empty, then the full display window will be used
instead.

## horizontalAlignment

 Determines whether the text is aligned to the left or
right of the text area, or centered within it.

## verticalAlignment

 Determines whether the text is aligned to the bottom or
top of the text area, or centered within it.

## transform

 A transformation applied to the entire text area after
layout has been performed. The translate and pivot values
are specified in pixels, and the rotate value is specified
in degrees.
