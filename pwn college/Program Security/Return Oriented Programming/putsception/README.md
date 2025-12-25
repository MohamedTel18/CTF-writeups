# Putsception Exploit Explanation

## Overview
This is a **two-stage ROP (Return-Oriented Programming) exploit** that leaks the libc address and then gains shell access to a vulnerable binary.

## Stage 1: Libc Leak

**Setup:**
- Loads the target binary and libc into pwntools
- Finds ROP gadgets: `pop rdi; ret` and `ret` (for stack alignment)
- Creates a 136-byte padding buffer (128 'A's + 8 'B's) to overflow the stack

**Payload Construction:**
```
[padding] → [ret] → [pop rdi] → [puts GOT] → [puts PLT] → [_start]
```

**Execution:**
1. Overwrites return address with ROP gadgets
2. Sets `rdi = puts@GOT` (address of puts in Global Offset Table)
3. Calls `puts()` via PLT to print the leaked address
4. Returns to `_start` to allow a second overflow

**Result:** Leaks the runtime address of `puts()` in libc, allowing calculation of the libc base address.

## Stage 2: Shell Execution

Using the leaked libc base, the exploit constructs:

```
[padding] → [ret] → [pop rdi] → [0] → [setuid] → [ret] → [pop rdi] → [/bin/sh] → [system] → [exit]
```

**Execution:**
1. Calls `setuid(0)` to gain root privileges
2. Calls `system("/bin/sh")` to spawn an interactive shell
3. Calls `exit()` for clean termination

**Result:** Gains interactive shell access with elevated privileges.

## Summary
The exploit demonstrates classic **information leak + ROP chain** techniques to bypass ASLR and execute arbitrary code.