FROM ubuntu:24.04

RUN apt-get update && apt-get install -y \
    libseccomp-dev socat \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /src

ENV LD_LIBRARY_PATH=/opt/libc

COPY director_hard /src/director_hard
COPY flag.txt flag.txt
RUN chmod 644 flag.txt

COPY libc.so.6 /src/libc.so.6
COPY ld-linux-x86-64.so.2 /src/ld-linux-x86-64.so.2

RUN chmod +x /src/ld-linux-x86-64.so.2

EXPOSE 1337

CMD ["socat","TCP-LISTEN:1337,reuseaddr,fork","EXEC:'/src/ld-linux-x86-64.so.2 --library-path /src /src/director_hard',pty,raw,echo=0,stderr"]
