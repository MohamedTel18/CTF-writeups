FROM ubuntu:24.04

RUN apt-get update && apt-get install -y \
    libseccomp-dev socat \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /src

COPY director_easy /src/director_easy
COPY flag.txt flag.txt
RUN chmod 644 flag.txt

EXPOSE 1337

CMD ["socat","TCP-LISTEN:1337,reuseaddr,fork","EXEC:'/src/director_easy',pty,raw,echo=0,stderr"]


