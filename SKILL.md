---
name: quiet-ui
description: "Use before writing or reviewing any user-facing string: remove implementation notes, obvious qualifiers, and narrated basics, and move secondary detail to an info icon or the help page."
---

# Quiet UI

The interface is not a design note, a changelog, or an apology. A string earns
its place only when it helps the user act or recover from a failure.

## When to use

Load this when you:

- add or edit a label, status line, empty state, tooltip, or note;
- build a settings screen, form, dialog, or single-window utility;
- review a UI for text noise.

Pair it with the antislop skills when the task is broader than text.

## The test

Before adding a string, answer one question:

**If the user ignores this text, do they fail to do what they came to do?**

If no, remove it. Then decide whether the fact belongs in an info icon or the
help page. If neither, it belongs nowhere.

## Workflow

1. **Inventory.** List every visible string: labels, placeholders, status
   messages, tooltips, notes, headings, and empty states.
2. **Classify.** Mark each as action, state, constraint, or explanation. The
   explanations are the ones to challenge.
3. **Apply the test.** Cut anything the user can act without.
4. **Place the rest.** Follow `references/placement.md`: an info icon for one
   fact needed in context, the help page for anything longer.
5. **Re-read as a user.** Cut any sentence that repeats a control, names the
   obvious, or explains the implementation.
6. **Verify.** Errors and destructive confirmations still say what failed and
   what to do next.

## Cut on sight

- Implementation notes: "Images are cached in IndexedDB.", "Built with
  Electron."
- Obvious qualifiers: "in any workspace", "here", "simply", "just".
- Narrated basics: "Click a file to open it."
- Defensive disclaimers: "Results may vary."
- Tooltips that repeat a label.

The full pattern list, with reasons: `references/patterns.md`.

## Keep

- Errors: what failed and the next step.
- Destructive confirmations.
- Empty states that name the next action.
- Constraints that apply at that moment, such as a disabled control with a
  reason.
- Units and formats: "MB", "mm", "24-hour time".

Placement rules: `references/placement.md`.

## Checklist

- [ ] Every visible string helps the user act or recover.
- [ ] No text explains how the app works.
- [ ] No label restates a visible control.
- [ ] No "on this screen", "here", or "simply".
- [ ] Secondary detail is in an info icon or the help page.
- [ ] A competent user would not be annoyed to read it twice.

Worked examples: `references/examples.md`.
