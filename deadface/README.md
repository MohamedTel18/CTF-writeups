## Deadface CTF - Lockpick Exploit Writeup

### Overview
This folder contains a writeup and exploit for the `lockpick` binary challenge from Deadface CTF.

### Files
- `lockpick`: The vulnerable binary provided in the challenge (Linux ELF, x86_64).
- `exploit.py`: Python script using pwntools to exploit the binary remotely.

### Vulnerability & Exploit
The `lockpick` binary is vulnerable to a buffer overflow. By sending a carefully crafted payload, we can overwrite the return address and control the execution flow.

#### Exploit Steps
1. **Buffer Overflow**: The exploit sends 72 bytes of padding (`A` characters) to overflow the buffer and reach the return address.
2. **ROP Chain**: The payload then places a ROP (Return-Oriented Programming) chain:
	- The chain calls several functions in the binary (`pick3`, `pick5`, `pick4`, `pick1`, `pick2`) in a specific order.
	- It uses a gadget at `0x40101a` to control the flow.
	- Finally, it jumps to `0x401407` the address of the line to check the values of variables pinX.
3. **Remote Exploitation**: The script connects to the challenge server (`env01.deadface.io:9999`) and sends the payload.
4. **Interactive Session**: After sending the payload, the script switches to interactive mode to receive the flag or shell.

#### Usage
Run the exploit with:
```bash
python3 exploit.py
```
Ensure you have `pwntools` installed (`pip install pwntools`).

### Notes
- The exact function order and addresses may depend on the binary version.
- The exploit assumes the binary is running on the remote server and symbols are not stripped.

---
This writeup explains the logic behind the exploit and how it leverages the buffer overflow vulnerability in the `lockpick` binary.

