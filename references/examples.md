# Worked examples

## Photo gallery

Before: `Images are cached in IndexedDB.`

After: nothing. The help page explains offline behavior.

Why: the cache name is machinery the user cannot act on.

## Search field

Before: `Search all files on your computer`

After: nothing, or `Search files`.

Why: the field label and placeholder already say what it searches.

## Note editor

Before: `Type a note, then press Save.`

After: nothing. The editor and the Save button show the step.

Why: the sentence narrates the interface.

## Music player

Before: `Playing. Press Pause to pause.`

After: `Playing.`

Why: the button already says Pause. The state is the useful part.

## Save tooltip

Before: a `Save` button with the tooltip `Save the note`.

After: no tooltip, or `Ctrl+S`.

Why: a tooltip must add a fact the label cannot carry.

## Billing error

Before: `Oops! Something went wrong.`

After: `Card declined. Check the number and try again.`

Why: the second version names the failure and the next step.

## Disabled delete

Before, always visible: `Note: deleting requires the file to be closed.`

After, shown only when the control is disabled: `Close the file in the other
app to delete it.`

Why: the constraint appears when it applies, with an action.

## Settings dialog

Before: a dialog titled `Settings`, a heading `Settings`, and a line `Change
your settings below.`

After: the dialog title and the controls. No heading, no line.

Why: the title and the controls are the interface. The heading and the sentence
repeat them.

## First run

Before: a permanent paragraph under the title: `Welcome! This is a notes app.
Type a note, then press Save.`

After: nothing, or a first-run empty state: `No notes yet. Press New note.`

Why: orientation belongs to the first run, not to every session.
