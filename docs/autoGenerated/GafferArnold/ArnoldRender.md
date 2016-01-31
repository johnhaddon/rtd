# ArnoldRender

Performs offline batch rendering using the
Arnold renderer. This is done in two phases -
first a .ass file is generated and then Arnold
is invoked to render it. Note though that the .ass
file is lightweight, and contains little more than
a procedural which will use Gaffer to generate the
scene at render time.

