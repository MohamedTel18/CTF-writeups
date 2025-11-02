## Feather-Father Challenge Writeup

### Challenge Overview
This challenge is a classic ret2libc (return-to-libc) exploitation scenario. The goal is to exploit a buffer overflow vulnerability in the `chall` binary to execute arbitrary code and gain a shell.

### Files
- `chall`: The vulnerable binary.
- `libc.so.6`, `ld-linux.so.2`: Provided libraries for remote exploitation.
- `exploit2.py`: Python script using pwntools to automate the exploit.

### Vulnerability & Exploit Technique
The binary contains a buffer overflow that allows overwriting the return address. By leveraging this, we can:
1. Leak the address of `puts` from the Global Offset Table (GOT) to determine the base address of libc.
2. Use the calculated libc base to call `system('/bin/sh')` and spawn a shell.

#### Exploit Steps (`exploit2.py`)
1. **Stage 1: Leak puts address**
	- Send a payload that calls `puts(puts@got)` and then returns to the vulnerable function (`vuln`).
	- Receive the leaked address of `puts` from the remote server.
2. **Stage 2: ret2libc attack**
	- Calculate the base address of libc using the leaked `puts` address.
	- Build a payload to call `system('/bin/sh')` with the correct addresses for `system`, `exit`, and the string `/bin/sh` from libc.
	- Send the payload to the server, which executes `system('/bin/sh')` and gives a shell.

#### Usage
Run the exploit with:
```bash
python3 exploit2.py
```
Ensure you have `pwntools` installed (`pip install pwntools`).

### Notes
- The exploit uses two stages: first to leak an address, second to gain code execution.
- The provided `libc.so.6` must match the remote server's libc for address calculations to work.
- The script handles timing and prompt detection to ensure reliable exploitation.

---
This writeup explains the ret2libc technique and how the exploit script automates the process to gain a shell on the remote server.
