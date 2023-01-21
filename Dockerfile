FROM python:3
RUN pip install flask
COPY mainscore.py /app/
COPY scores.txt /app/
WORKDIR /app/
CMD python mainscore.py
