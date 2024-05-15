FROM ubuntu:latest
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=UTF-8
RUN apt-get update \
&& apt-get -y upgrade \
&& apt-get -y install python3
ADD server.tar.gz /
CMD [ "python3", "/server_side.py", "8888" ]
