FROM python:3.13-slim
WORKDIR /work
COPY backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY backend/ ./
CMD ["python", "-m", "pytest", "-q", "--ledger-postgres"]
