# Patterns to cut

Each entry has a tell, a reason, and a fix. The reason matters more than the
phrase: the same noise appears in many words.

## Implementation notes

**Tell:** "A fullscreen app covers this window. The keys still work.", "Uses
the compositor portal", "The device is created through uinput".

**Why:** the user does not care how it works or what might cover it. A
permanent note about a limitation reads as an excuse and costs reading on every
session.

**Fix:** delete it. If the fact changes what the user can do, move it to the
help page or behind an info icon.

## Obvious qualifiers

**Tell:** "in any app", "on your screen", "click here", "press the button",
"simply", "just".

**Why:** the control already says it. "F5 starts in any app" explains what a
global key is to someone who already set one.

**Fix:** state the noun and the action, or say nothing when the field label
already carries it.

## Narrated basics

**Tell:** "Click Start to begin", "Enter a number", "Select a mouse button",
"This window lets you...".

**Why:** it treats a competent user as someone who needs the interface read
aloud, and it pushes the real controls down the window.

**Fix:** delete. Labels and standard controls carry the meaning.

## Defensive disclaimers

**Tell:** "Results may vary", "This may not work on every system", "Note: this
feature depends on your desktop".

**Why:** a warning before anything goes wrong is noise. When something does go
wrong, the user needs the specific failure, not a general hedge.

**Fix:** keep only a constraint that prevents a real error, and show it when it
applies. Put the rest in the help page.

## Label-echo tooltips

**Tell:** a "Start" button with the tooltip "Start the clicker".

**Why:** the tooltip is a second copy of the same words.

**Fix:** no tooltip, or a tooltip that adds information the label cannot, such
as the exact key that fires.

## Status messages that repeat the controls

**Tell:** "Running. F6 or Stop ends it." while the button reads STOP and the
stop field reads F6.

**Why:** the state is useful; the instructions are not. The user can see the
button and the key.

**Fix:** "Running." Keep the count, the failure, or the next step.

## Onboarding paragraphs

**Tell:** a two-sentence welcome under the title of a one-window utility.

**Why:** the user opened the tool to use it, not to read about it.

**Fix:** delete. If a first step is genuinely required, make it the empty state
with one action.

## Apologies and hedges

**Tell:** "Sorry, something went wrong", "Oops!", "It seems that...", "This
may take a moment".

**Why:** an apology does not tell the user what failed or what to do. A hedge
makes a specific failure sound uncertain.

**Fix:** name the failure and the next step: "Could not open /dev/uinput. Run
the setup script, then log in again."

## Redundant headings

**Tell:** "Settings" as the only heading inside a settings window, "Actions"
above a single button.

**Why:** the window title and the control already carry the label.

**Fix:** remove the heading, or make it name a real group.

## Technical boilerplate in the main view

**Tell:** portal names, kernel modules, API versions, file paths, and protocol
details shown to the user by default.

**Why:** the user needs the outcome, not the machinery. Technical detail
belongs in the help page or a diagnostic view.

**Fix:** replace it with the user-visible consequence, or move it.

## Success text that congratulates itself

**Tell:** "Success! Your settings were saved successfully."

**Why:** the first word already says it. The rest repeats the word.

**Fix:** "Saved." Stop there.
