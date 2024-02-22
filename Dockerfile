FROM python:3.12

WORKDIR /etl-fhir

COPY requirements.txt .

RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

ENV PYTHONPATH "${PYTHONPATH}:/etl-fhir"

LABEL maintainer="Abu Hamza" \
      version="1.0"

ENTRYPOINT ["python", "src/__main__.py"]