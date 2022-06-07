FROM python:3

WORKDIR /usr/src/app

COPY findCycles.py requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "findCycles.py"] 