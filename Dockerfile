FROM grahamdumpleton/mod-wsgi-docker:python-2.7-onbuild
RUN ln -s /run/secrets/gz_nodes.cfg /app/instance/gz_nodes.cfg
CMD ["gz_nodes_wsgi.py"]
