# LocalDispatcher

Schedules execution of task graphs on the local machine. Tasks
may be dispatched in the background to keep the UI responsive.

## user

 Container for user-defined plugs. Nodes
should never make their own plugs here,
so users are free to do as they wish.

## framesMode

 Determines the active frame range to be dispatched as
follows :

  - CurrentFrame uses the current timeline frame only.
  - FullRange uses the outer handles of the timeline
    (i.e. the full range of the script).
  - CustomRange uses a user defined range, as specified by
    the frameRange plug.

## frameRange

 The frame range to be used when framedMode is "CustomRange".

## jobName

 A descriptive name for the job.

## jobsDirectory

 A directory to store temporary files used by the dispatcher.

## executeInBackground

 Executes the dispatched tasks in separate processes via a
background thread.

## ignoreScriptLoadErrors

 Ignores errors loading the script when executing in the background.
This is not recommended - fix the problem instead.

