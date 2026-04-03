FROM python:3.10
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code

# CRITICAL: This tells the container where to find your custom environment files
ENV PYTHONPATH="/code"

# CRITICAL: Hugging Face Spaces requires port 7860
CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"]