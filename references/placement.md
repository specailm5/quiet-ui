# Where extra information goes

The window has three places for a fact, and the most common answer is the
fourth: nowhere.

| The fact is... | Put it... |
| --- | --- |
| Needed to complete the current action | Next to the control, behind an info icon |
| A consequence of the action the user is about to take | Inline, at the control |
| A failure | Inline, where the failure appears |
| Background, a limitation, setup, or a longer explanation | The help page or README |
| A repeat of a visible label or state | Nowhere |
| A one-time orientation step | The first-run empty state or the help page |

## Info icon

Use it for one fact the user may need while working.

- The icon sits next to the control it explains.
- The tooltip or popover holds one or two sentences.
- The text adds something the label cannot: a consequence, a limit, a shortcut.
- It does not repeat the label.
- It is reachable by keyboard and has an accessible name.

If the fact needs a paragraph, it is not an info icon. It is a help page.

## Help page

Use it for everything longer than a sentence.

- Setup, requirements, platform limits, undo steps, and troubleshooting.
- The main window may link to it, but it does not summarize it.
- A link labeled "Help" is enough. Do not paste the help text into the window.

## Inline

Inline text is for the current state or the current failure.

- Errors: what failed, and the next step.
- Destructive consequences: what will be lost.
- Constraints: why the control is disabled, at the moment it is disabled.
- Success: a short confirmation, then stop.

## Nowhere

Cut the fact when the user can act without it. That is the default.
