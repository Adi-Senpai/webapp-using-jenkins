FROM python
RUN mkdir app
COPY . /app/
EXPOSE 5000
RUN pip install -r /app/requirements.txt
ENTRYPOINT ["python"]
CMD ["/app/app.py"]