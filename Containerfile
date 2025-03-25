# syntax=docker/dockerfile:experimental
FROM python:3.12-alpine
COPY data/ ./data/
COPY requirements.txt debrief.py .
RUN --mount=type=cache,target=/cache --mount=type=tmpfs,target=/temp \
  TMPDIR=/temp python -m pip install --cache-dir=/cache -r ./requirements.txt
CMD python debrief.py