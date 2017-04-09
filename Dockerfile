FROM continuumio/anaconda3
RUN /opt/conda/bin/conda install jupyter -y --quiet && mkdir /opt/notebooks
ADD jupyter_notebooks/ /opt/notebooks
CMD ["jupyter", "notebook", "--notebook-dir=/opt/notebooks", "--ip='*'", "--port=8888", "--no-browser"]