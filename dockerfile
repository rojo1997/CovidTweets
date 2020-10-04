FROM python:latest as covi_tweets
RUN apt-get update && apt-get install -y \
    git \
    uwsgi \
    uwsgi-src && \
    apt-get clean
ADD . /CoviTweets
RUN python3 -m pip install -r /CoviTweets/requirements.txt && \
    export PYTHON=python3.8 && \
    uwsgi --build-plugin "/usr/src/uwsgi/plugins/python python38" && \
    mv python38_plugin.so /usr/lib/uwsgi/plugins/python38_plugin.so && \
    chmod 644 /usr/lib/uwsgi/plugins/python38_plugin.so
WORKDIR /CoviTweets/CoviTweets/
EXPOSE 5000
CMD [ "uwsgi", "--ini", "server.ini"]