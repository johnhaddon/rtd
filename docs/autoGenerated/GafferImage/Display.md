# Display

Interactively displays images as they are rendered.

This node runs a server on a background thread,
allowing it to receive images from both local and
remote render processes. To set up a render to
output to the Display node, use an Outputs node with
an Interactive output configured to render to the
same port as is specified on the Display node.

