FROM ubuntu:18.04
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip
RUN useradd -ms /bin/bash celery
USER celery
WORKDIR /home/celery
ENV PATH="/home/celery/.local/bin:${PATH}"
RUN pip install --upgrade pip
COPY . /home/celery
RUN pip3 install --no-cache -r requirements.txt
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
EXPOSE 5000
EXPOSE 5555
#CMD ["./main.sh"]
CMD ["supervisord"]