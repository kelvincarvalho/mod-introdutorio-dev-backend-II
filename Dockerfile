FROM python:3.12

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

ENTRYPOINT ["tail", "-f", "/dev/null"]