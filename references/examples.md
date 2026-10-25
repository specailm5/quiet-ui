# Worked examples

## Desktop utility

Before: `A fullscreen app covers this window. The keys still work.`

After: nothing in the window. The README explains fullscreen behavior.

Why: the note describes a stacking rule the user cannot change, and the keys
already work. It is an implementation note with a reassurance attached.

## Global shortcut status

Before: `F5 starts, F6 stops, in any app`

After: nothing. The fields read `Start key F5` and `Stop key F6`.

Why: the fields are the source of truth. "In any app" explains what a global
shortcut is to the person who just set one.

## Start button

Before: `Click Start to begin clicking.`

After: nothing. The button says `Start`.

Why: the label is the instruction.

## Success

Before: `Success! Your settings were saved successfully.`

After: `Saved.`

Why: one word confirms the result. The rest repeats it.

## Error

Before: `Oops! Something went wrong.`

After: `Could not open /dev/uinput. Run the setup script, then log in again.`

Why: the second version names the failure and the next step.

## Disabled control

Before, always visible: `Note: the stop key needs the GlobalShortcuts portal.`

After, shown only when the binding fails: `Keys unavailable: the desktop
denied the binding. Use the buttons.`

Why: the constraint appears when it applies, with an action.

## Tooltip

Before: a `Start` button with the tooltip `Start the clicker`.

After: no tooltip, or `F5 also starts it.`

Why: a tooltip must add a fact the label cannot carry.

## Settings

Before: a dialog titled `Settings`, a heading `Settings`, and a line `Change
your settings below.`

After: the dialog title and the controls. No heading, no line.

Why: the title and the controls are the interface. The heading and the sentence
repeat them.

## Onboarding

Before: a permanent paragraph under the title: `Welcome! This tool repeats
mouse clicks. Choose an interval, then press Start.`

After: nothing, or a first-run empty state: `No runs yet. Press Start to begin.`

Why: orientation belongs to the first run, not to every session.
