FROM python:3
#RUN apt-get update
#RUN apt-get install -y apt-utils 
#RUN apt-get install -y --no-install-recommends apt-transport-https ca-certificates curl software-properties-common python3-pip wget unzip jq dnsmasq apt-utils
#RUN apt-get install -y python
#RUN apt-get install -y net-tools
#RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
#RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
#RUN apt-get update
#RUN DEBIAN_FRONTEND=noninteractive apt-get install -y docker-ce
#RUN export IP=$(hostname -I | cut -d\  -f1)
#RUN sed -i -e "s/-H fd:\/\//-H fd:\/\/ -H tcp:\/\/$IP:2375/g" /lib/systemd/system/docker.service
#RUN service docker start
RUN pip install requests
#RUN pip3 install requests
ADD my_script.py /
ADD app.py /
#CMD [ "python", "./my_script.py" ]
