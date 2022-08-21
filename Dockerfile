FROM python

WORKDIR /PycharmProjects

COPY . .

CMD ["python","main.py"]