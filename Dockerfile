FROM python:3.11-slim

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "test_orchestrator.py"]

# Set default arguments (optional)
CMD ["default_arg1", "default_arg2"]