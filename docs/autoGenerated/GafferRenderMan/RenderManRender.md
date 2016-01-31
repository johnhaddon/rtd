# RenderManRender

Performs offline batch rendering using a
RenderMan renderer. This is done in two
phases - first a RIB file is generated and
then the renderer is invoked to render it in
a separate process. Note though that the RIB
file is lightweight, and contains a single
procedural which will invoke Gaffer to generate
the scene on demand at runtime. The RIB therefore
requires very little disk space.

