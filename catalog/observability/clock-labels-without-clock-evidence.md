# Timestamp labels disagree with the actual clock

[Catalog](../README.md) / [observability](README.md) / clock-labels-without-clock-evidence

**Go here if:** A ruling, brief or receipt has a time ahead of the clock, a guessed label or a quoted clock value no call returned.

**Rule:** Generate each timestamp directly from a completed clock read and mechanically compare the written label with that returned value; never estimate it, type it from memory or schedule its write alongside the read.

15 incidents, 15 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0274](../../incidents/INC-0274-write-times-from-a-command-output-not-from-memory.md) - Write times from a command output, not from memory
- occurrences 10, severity medium, status fixed
- **Signature:** An evidence line recorded a time that was not read from a clock.
- **Rule:** Write a recorded time from a command output, never from memory
- **Recurrences:**
  - [INC-0350](../../incidents/INC-0350-time-stamps-written-from-an-estimate-ran-ahead-of-the-clock.md) - 2026-11-01 - Time stamps written from an estimate ran ahead of the clock
  - [INC-0373](../../incidents/INC-0373-two-replies-were-stamped-with-times-ahead-of-the-clock.md) - 2026-11-01 - Two replies were stamped with times ahead of the clock
  - [INC-0383](../../incidents/INC-0383-a-ruling-was-stamped-four-minutes-ahead-of-the-clock-because.md) - 2026-11-01 - A ruling was stamped four minutes ahead of the clock because the time was written before the clock was read
  - [INC-0384](../../incidents/INC-0384-the-lead-stamped-a-brief-four-minutes-ahead-of-the-clock-aga.md) - 2026-11-01 - The lead stamped a brief four minutes ahead of the clock again, one round after the same correction
  - [INC-0415](../../incidents/INC-0415-a-ruling-timestamp-was-written-from-an-estimate-and-correcte.md) - 2026-11-02 - A ruling timestamp was written from an estimate and corrected minutes later, twice in one round
  - [INC-0442](../../incidents/INC-0442-the-lead-wrote-a-ruling-timestamp-before-reading-the-clock.md) - 2026-11-02 - The lead wrote a ruling timestamp before reading the clock
  - [INC-0456](../../incidents/INC-0456-the-lead-wrote-ruling-timestamps-from-memory-three-times-and.md) - 2026-11-02 - The lead wrote ruling timestamps from memory three times and had to correct them
  - [INC-0567](../../incidents/INC-0567-heading-times-in-several-rulings-and-briefs-ran-thirty-to-se.md) - 2026-11-04 - Heading times in several rulings and briefs ran thirty to seventy minutes ahead of the real clock
  - [INC-0606](../../incidents/INC-0606-ruling-labels-written-from-an-estimated-clock-ran-up-to-six.md) - 2026-11-04 - Ruling labels written from an estimated clock ran up to six minutes ahead of the real clock

### [INC-0611](../../incidents/INC-0611-a-time-label-was-written-in-the-same-script-that-read-the-cl.md) - A time label was written in the same script that read the clock afterwards, minutes after a rule to read the clock first was recorded
- occurrences 4, severity low, status mitigated
- **Signature:** A time label is later than the clock read in the same script.
- **Rule:** Read the clock in its own call and copy that value into the label; a rule that exists is not a check.
- **Recurrences:**
  - [INC-0613](../../incidents/INC-0613-a-time-label-was-typed-in-the-same-parallel-batch-of-calls-t.md) - 2026-11-04 - A time label was typed in the same parallel batch of calls that read the clock, so it was written before the clock was seen; the third recurrence
  - [INC-0617](../../incidents/INC-0617-a-ruling-quoted-a-clock-value-that-was-never-read-because-th.md) - 2026-11-04 - A ruling quoted a clock value that was never read, because the write ran in the same parallel batch as the clock call; the fourth recurrence
  - [INC-0619](../../incidents/INC-0619-a-clock-label-slip-recurred-a-fifth-time-and-the-clock-call.md) - 2026-11-04 - A clock label slip recurred a fifth time, and the clock call became the only call in its batch

### [INC-0624](../../incidents/INC-0624-the-clock-call-ran-alone-in-its-own-message-yet-the-ruling-l.md) - The clock call ran alone in its own message, yet the ruling label was typed from expectation instead of copied from the returned value; the seventh recurrence
- occurrences 1, severity low, status mitigated
- **Signature:** A heading time differs from the clock output returned just before it.
- **Rule:** Copy a time label from the returned clock output, never type it; make the check mechanical by comparing the heading's time with the last clock output.
