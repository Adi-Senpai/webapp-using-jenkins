FROM python
RUN Mkdir /app
COPY . /app/app.py
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["/app/app.py"]