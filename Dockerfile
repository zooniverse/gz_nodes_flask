FROM grahamdumpleton/mod-wsgi-docker:python-2.7-onbuild
RUN mkdir -p /app/instance/
CMD ["gz_nodes_wsgi.py"]
