FROM continuumio/anaconda3
RUN mkdir -p /root/workspace/
ADD requirements.txt /root/workspace/
ADD start.sh /root/workspace/
WORKDIR /root/workspace
RUN conda install jupyter -y --quiet \ 
 && mkdir notebooks \
 && pip install -q -r requirements.txt
CMD ["/bin/bash", "/root/workspace/start.sh"]