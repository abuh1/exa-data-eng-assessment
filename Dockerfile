FROM python:3.12

WORKDIR /etl-fhir

COPY . .

RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir --upgrade -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/etl-fhir"
ENV DOCKER_CONTAINER="True"

ENV DB_USER=
ENV DB_PASS=
ENV DB_NAME=
ENV DB_HOST=
ENV DB_PORT=

LABEL maintainer="Abu Hamza" \
      version="1.0"

ENTRYPOINT ["python", "src/__main__.py"]