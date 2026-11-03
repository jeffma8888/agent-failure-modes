---
id: INC-0558
title: Two agents cancelled their queued heavy jobs by task id during a pause, but the queued shells survived; one later took the host lock and ran its test after the agent had reported it cancelled
date: 2026-11-02
classes: [concurrency, ipc-and-env, observability]
severity: low
status: open
---

# INC-0558 - Two agents cancelled their queued heavy jobs by task id during a pause, but the queued shells survived; one later took the host lock and ran its test after the agent had reported it cancelled

**Cost:** A browser test ran after the team was told to pause, and the agent's checkpoint said the job was cancelled; the lead found the run only by reading log timestamps against the report.

## Signature - how you recognise it

A job reported as cancelled has a log whose first line is written after the cancellation time, or its shell PIDs still answer ps.

## What happened

When the operator paused the team, each agent cancelled its own queued runtime job by exact task id, as the pause rules required. The jobs were queued behind the shared host lock, so the cancelled task wrapper had launched shells that were still polling for the lock. One agent checked ps after cancelling, found its two queued shells still alive, and sent SIGTERM to those exact PIDs. The other agent wrote its checkpoint ("cancelled while waiting for lock") without that check. About a minute later its queued shell acquired the lock (lock wait 50 seconds, load1 13), ran migrations, seeded a database and ran three browser tests, and wrote a complete log after the checkpoint. The work was harmless (an expected failing test on unchanged code), but it ran after the pause and against the written state.

## Root cause

Cancelling the task wrapper did not signal the process group it had started, and a long lock queue keeps a cancelled job alive long enough to become runnable later.

## Why it was hard to see

The cancellation returns a success notification and the log is empty at that moment, so both available signals say the job is gone; the shell is only visible to ps, by PID.

## Fix

After cancelling any queued or running job, list its recorded PIDs and the lock owner, and signal the exact PIDs that remain; have the lock helper exit when its parent task is gone.

## Verification

Checked by the person who reported it, from the log timestamps and the lock line in the log. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A cancellation is complete only when the job's own PIDs are gone from ps; record that check in the checkpoint, and make any helper that waits on a lock exit when its parent dies.

## Related

[INC-0556](./INC-0556-a-polling-host-lock-does-not-serve-waiters-in-order-so-a-tes.md) [INC-0557](./INC-0557-the-lock-holder-waited-for-the-load-to-fall-while-still-hold.md)
