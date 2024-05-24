FROM python:3.12-slim

ARG USERNAME=pawel
RUN groupadd -r $USERNAME && useradd -m -r -g $USERNAME:$USERNAME && \
    apt-get update && apt-get -y install -qq --force-yes cron && \
    apt-get -y install -qq --force-yes procps htop less nano micro watch curl

ADD src/crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab && \
    crontab -u $USERNAME /etc/cron.d/crontab && \
    chmod u+s /usr/sbin/cron

WORKDIR /app

COPY requirements/prod.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .
RUN chmod a+x run_services.sh

USER $USERNAME

CMD ./run_services.sh
