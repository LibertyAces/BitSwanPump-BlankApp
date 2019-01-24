FROM teskalabs/bspump:master-alpine3.8
MAINTAINER TeskaLabs Ltd (support@teskalabs.com)

# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8

RUN set -ex \
	mkdir /opt/bspump-example

COPY ./bspump-example.py /opt/bspump-example/bspump-example.py
COPY ./sample.csv /opt/bspump-example/sample.csv


WORKDIR /opt/bspump-example
CMD ["python3", "/opt/bspump-example/bspump-example.py", "-w"]
