# Teammates finished on disk; the reply never came or went unnoticed

[Catalog](../README.md) / [delegation](README.md) / finished-on-disk-no-reply

**Go here if:** A thread shows finished or paused with no message, a reply arrived while you were busy and was never read, an output file stopped changing, or you are about to end a turn waiting on a message.

**Rule:** Never treat a reply as the only signal of completion. Discriminators: when a teammate shows finished or paused, or its output file stops changing, read the file and the run state at once and grade from disk; check who spoke last per teammate instead of assuming silence means running; read a real clock; never end a turn waiting on a message alone.

6 incidents, 6 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0128](../../incidents/INC-0128-finished-work-sat-for-hours-because-replies-never-arrived-th.md) - Finished work sat for hours because replies never arrived, the clock was misread and worktrees were not swept
- occurrences 5, severity medium, status fixed
- **Signature:** Several teammates finish, no reply arrives, and the lead waits.
- **Rule:** Sweep the disk and read a real clock before trusting replies.
- **Recurrences:**
  - [INC-0317](../../incidents/INC-0317-finished-teammates-sat-unnoticed-because-their-completion-re.md) - 2026-11-01 - Finished teammates sat unnoticed because their completion replies never arrived
  - [INC-0416](../../incidents/INC-0416-ten-teammate-threads-showed-state-paused-with-complete-outpu.md) - 2026-11-02 - Ten teammate threads showed state paused with complete outputs on disk and no reply message
  - [INC-0573](../../incidents/INC-0573-teammate-replies-stopped-reaching-the-lead-for-about-25-minu.md) - 2026-11-04 - Teammate replies stopped reaching the lead for about 25 minutes while their files landed on disk
  - [INC-0630](../../incidents/INC-0630-a-lead-ended-its-turn-waiting-for-a-reviewer-s-completion-me.md) - 2026-11-07 - A lead ended its turn waiting for a reviewer's completion message while the reviewer's finished files were already on disk, and nothing moved for days

### [INC-0091](../../incidents/INC-0091-teammate-replies-arrived-while-the-lead-was-busy-and-were-mi.md) - Teammate replies arrived while the lead was busy and were missed, leaving finished work idle for about 30 minutes
- occurrences 1, severity medium, status fixed
- **Signature:** A teammate finished and replied, but the lead assumed work was still in flight.
- **Rule:** Verify the last speaker per teammate instead of assuming no news means work is running.
