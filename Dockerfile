FROM python:3.6

WORKDIR /usr/src/app

COPY pyserver.py ./
COPY textgenrnn_weights.hdf5 ./
RUN pip3 install textgenrnn

RUN pip3 install --user --upgrade tensorflow

EXPOSE 9000

CMD [ "python3", "./pyserver.py" ]
