## Waddler Challenge Writeup

### Overview
This folder contains the solution and exploit for the `Waddler` binary challenge from v1t CTF.

### Files
- `chall1`: The vulnerable binary provided in the challenge.
- `exploit1.py`: Python script using pwntools to exploit the binary remotely.

### Vulnerability & Exploit
The `chall1` binary is vulnerable to a buffer overflow. By sending a crafted payload, we can overwrite the return address and redirect execution(ret2win).

#### Exploit Steps
1. **Buffer Overflow**: The exploit sends 72 bytes of padding (`A` characters) to overflow the buffer and reach the return address.
2. **Control Flow Hijack**: The payload then overwrites the return address with the address `0x40128c`, which points to a function that reveals the flag.
3. **Remote Exploitation**: The script connects to the challenge server (`chall.v1t.site:30210`) and sends the payload.


#### Usage
Run the exploit with:
```bash
python3 exploit1.py
```
Ensure you have `pwntools` installed (`pip install pwntools`).



---
This writeup explains the logic behind the exploit and how it leverages the buffer overflow vulnerability in the `chall1` binary.
