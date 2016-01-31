# OpenImageIOReader

Utility node which reads image files from disk using OpenImageIO.
All file types supported by OpenImageIO are supported by the
OpenImageIOReader.

## user

 Container for user-defined plugs. Nodes
should never make their own plugs here,
so users are free to do as they wish.

## out

 The output image generated by this node.

## enabled

 Turns the node on and off.

## fileName

 The name of the file to be read. File sequences with
arbitrary padding may be specified using the '#' character
as a placeholder for the frame numbers. If this file sequence
format is used, then missingFrameMode will be activated.

## refreshCount

 May be incremented to force a reload if the file has
changed on disk - otherwise old contents may still
be loaded via Gaffer's cache.

## missingFrameMode

 Determines how missing frames are handled when the input
fileName is a file sequence (uses the '#' character).
The default behaviour is to throw an exception, but it
can also hold the last valid frame in the sequence, or
return a black image which matches the data window and
display window of the previous valid frame in the sequence.

## availableFrames

 An output of the available frames for the given file sequence.
Returns an empty vector when the input fileName is not a file
sequence, even if it has a file-sequence-like structure.
