# ScriptNode

Defines a "script" - a Gaffer node network which can be
saved to disk as a ".gfr" file and reloaded.

## user

 Container for user-defined plugs. Nodes
should never make their own plugs here,
so users are free to do as they wish.

## fileName

 Where the script is stored.

## unsavedChanges

 Indicates whether or not the script has been
modified since it was last saved.

## frameRange

 Defines the start and end frames for the script.
These don't enforce anything, but are typically
used by dispatchers to control default frame
ranges, and by the UI to define the range of the
time slider.

## frameRange.start

 The start frame. This doesn't enforce anything,
but is typically used by dispatchers to control
default frame ranges, and by the UI to define
the range of the time slider.

## frameRange.end

 The end frame. This doesn't enforce anything,
but is typically used by dispatchers to control
default frame ranges, and by the UI to define
the range of the time slider.

## framesPerSecond

 The framerate used to convert between the current
frame number and the time in seconds.

## variables

 Container for user-defined variables which can
be used in expressions anywhere in the script.

