# 🚩 CTF Writeups Repository

<div align="center">

![CTF Banner](https://img.shields.io/badge/CTF-Writeups-red?style=for-the-badge)
![Pwn](https://img.shields.io/badge/Category-Pwn-blue?style=for-the-badge)
![Reverse Engineering](https://img.shields.io/badge/Category-Reverse-green?style=for-the-badge)

**A comprehensive collection of CTF writeups focused on Pwn and Reverse Engineering challenges**

</div>

---

## 📖 About This Repository

Welcome to my CTF Writeups repository! This is a curated collection of detailed solutions and explanations for binary exploitation (Pwn) and reverse engineering challenges from various Capture The Flag (CTF) competitions. 

The goal of this repository is to:
- 📚 Share knowledge and techniques in binary exploitation and reverse engineering
- 🎓 Help beginners learn from real-world CTF challenges
- 🤝 Build a collaborative community of security researchers and pwn enthusiasts
- 💡 Document different approaches and methodologies for solving challenges
- 🔍 Provide detailed explanations that go beyond just solutions

## 🎯 Categories

### 🔴 Pwn Challenges
Binary exploitation challenges focusing on:
- Buffer Overflows (Stack & Heap)
- Return-Oriented Programming (ROP)
- Format String Vulnerabilities
- Use-After-Free (UAF)
- Return-to-libc attacks
- Shellcoding
- ASLR/PIE bypasses
- Heap exploitation techniques

### 🔵 Reverse Engineering Challenges
Reverse engineering challenges covering:
- Static Analysis
- Dynamic Analysis with GDB/radare2
- Binary Decompilation
- Anti-debugging techniques
- Obfuscation analysis
- Malware analysis fundamentals
- Assembly language understanding
- Cryptographic algorithm reversing

## 📂 Repository Structure

```
CTF-writeups/
├── CTF-Name/
│   ├── Challenge-Name/
│   │   ├── README.md           # Detailed writeup
│   │   ├── exploit.py          # Exploit script
│   │   ├── challenge_binary    # Original challenge file
│   │   └── screenshots/        # Screenshots and images
│   └── ...
└── README.md
```

## 🚀 Getting Started

### Prerequisites
To follow along with these writeups, you should have basic knowledge of:
- Linux command line
- C programming language
- x86/x64 Assembly
- Python scripting (for exploits)

### Recommended Tools
- **GDB** with [pwndbg](https://github.com/pwndbg/pwndbg) or [GEF](https://github.com/hugsy/gef)
- **pwntools** - CTF framework for exploit development
- **radare2** / **Ghidra** / **IDA Pro** - Reverse engineering tools
- **ROPgadget** / **ropper** - ROP chain building tools
- **checksec** - Binary security property checker

### Installation
```bash
# Clone the repository
git clone https://github.com/YourUsername/CTF-writeups.git
cd CTF-writeups

# Install pwntools (Python)
pip install pwntools

# Install pwndbg (GDB enhancement)
git clone https://github.com/pwndbg/pwndbg
cd pwndbg
./setup.sh
```

## 📝 Writeup Format

Each writeup follows a consistent structure:

1. **Challenge Information**
   - Challenge name and category
   - CTF competition and date
   - Difficulty level
   - Points and solves

2. **Initial Analysis**
   - Binary security protections (checksec)
   - File type and architecture
   - Initial observations

3. **Vulnerability Discovery**
   - Detailed analysis of the vulnerability
   - How it was discovered
   - Proof of concept

4. **Exploitation**
   - Step-by-step exploitation process
   - Payload construction
   - Bypass techniques used

5. **Solution Script**
   - Complete exploit code with comments
   - Alternative approaches (if any)

6. **Flag**
   - The captured flag

7. **Key Takeaways**
   - Lessons learned
   - Similar challenges or techniques

## 🤝 Contributing

Contributions are welcome! If you have writeups you'd like to share:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/new-writeup`)
3. Add your writeup following the repository structure
4. Ensure your writeup is clear and well-documented
5. Commit your changes (`git commit -am 'Add writeup for XYZ challenge'`)
6. Push to the branch (`git push origin feature/new-writeup`)
7. Open a Pull Request

### Contribution Guidelines
- Writeups must be original work or properly attributed
- Include all necessary files (exploit scripts, binaries if allowed)
- Use clear and professional language
- Add screenshots/diagrams where helpful
- Test your exploit scripts before submitting
- Respect CTF rules (don't publish writeups during active competitions)

## 📚 Resources

### Learning Resources
- [pwn.college](https://pwn.college/) - Modern binary exploitation course
- [Nightmare](https://guyinatuxedo.github.io/) - Binary exploitation tutorial
- [ROP Emporium](https://ropemporium.com/) - ROP chain building practice
- [Microcorruption](https://microcorruption.com/) - Embedded security CTF

### Useful Links
- [CTFtime](https://ctftime.org/) - CTF competition tracker
- [Exploit Database](https://www.exploit-db.com/) - Exploit archive
- [Shellcode Database](http://shell-storm.org/shellcode/) - Shellcode collection
- [LiveOverflow](https://www.youtube.com/c/LiveOverflow) - Binary exploitation videos

## 🏆 CTF Platforms

Practice your skills on these platforms:
- [HackTheBox](https://www.hackthebox.com/)
- [TryHackMe](https://tryhackme.com/)
- [PicoCTF](https://picoctf.org/)
- [pwnable.kr](http://pwnable.kr/)
- [pwnable.tw](https://pwnable.tw/)
- [Exploit.Education](https://exploit.education/)

## 📊 Statistics

- **Total Writeups**: Coming soon
- **CTFs Covered**: Coming soon
- **Categories**: Pwn, Reverse Engineering
- **Last Updated**: December 2025



## 🙏 Acknowledgments

- All CTF organizers for creating amazing challenges
- The security research community for sharing knowledge
- Contributors who help improve these writeups

## 📧 Contact

- **GitHub**: [MohamedTel18](https://github.com/MohamedTel18)
- **Discord UserName**: mohi_telkhoukhe

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

*Built with ❤️ by the CTF community*

</div>
