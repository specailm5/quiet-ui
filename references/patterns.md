# Patterns to cut

Each entry has a tell, a reason, and a fix. The reason matters more than the
phrase: the same noise appears in many words.

## Implementation notes

**Tell:** "Images are cached in IndexedDB.", "Built with Electron.", "The
preview is rendered with WebGL."

**Why:** the user does not care how it works. A permanent note about the
machinery reads as a boast or an excuse and costs reading on every session.

**Fix:** delete it. If the fact changes what the user can do, move it to the
help page or behind an info icon.

## Obvious qualifiers

**Tell:** "in any workspace", "on this screen", "click here", "simply", "just".

**Why:** the control already says it. "Search all files on your computer" under
a field labeled "Search" explains the obvious.

**Fix:** state the noun and the action, or say nothing when the field label
already carries it.

## Narrated basics

**Tell:** "Click a file to open it", "Type a name to name the file", "Select a
color", "This window lets you...".

**Why:** it treats a competent user as someone who needs the interface read
aloud, and it pushes the real controls down the window.

**Fix:** delete. Labels and standard controls carry the meaning.

## Defensive disclaimers

**Tell:** "Results may vary", "This may not work on every network", "Note: this
feature depends on your device".

**Why:** a warning before anything goes wrong is noise. When something does go
wrong, the user needs the specific failure, not a general hedge.

**Fix:** keep only a constraint that prevents a real error, and show it when it
applies. Put the rest in the help page.

## Label-echo tooltips

**Tell:** a "Save" button with the tooltip "Save the note".

**Why:** the tooltip is a second copy of the same words.

**Fix:** no tooltip, or a tooltip that adds information the label cannot, such
as the keyboard shortcut "Ctrl+S".

## Status messages that repeat the controls

**Tell:** "Playing. Press Pause to pause." while the button reads Pause.

**Why:** the state is useful; the instructions are not. The user can see the
button.

**Fix:** "Playing." Keep the count, the failure, or the next step.

## Onboarding paragraphs

**Tell:** a two-sentence welcome under the title of a notes app.

**Why:** the user opened the app to use it, not to read about it.

**Fix:** delete. If a first step is genuinely required, make it the empty state
with one action.

## Apologies and hedges

**Tell:** "Sorry, something went wrong", "Oops!", "It seems that...", "This
may take a moment".

**Why:** an apology does not tell the user what failed or what to do. A hedge
makes a specific failure sound uncertain.

**Fix:** name the failure and the next step: "Card declined. Check the number
and try again."

## Redundant headings

**Tell:** "Settings" as the only heading inside a settings window, "Files"
above a file list.

**Why:** the window title and the list already carry the label.

**Fix:** remove the heading, or make it name a real group.

## Technical boilerplate in the main view

**Tell:** cache names, rendering engines, API versions, file paths, and
protocol details shown to the user by default.

**Why:** the user needs the outcome, not the machinery. Technical detail
belongs in the help page or a diagnostic view.

**Fix:** replace it with the user-visible consequence, or move it.

## Success text that congratulates itself

**Tell:** "Success! Your note was saved successfully."

**Why:** the first word already says it. The rest repeats the word.

**Fix:** "Saved." Stop there.
