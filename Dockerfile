# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the DAG and job files
COPY dags/ pipeline.py /app/dags/
COPY jobs/ /app/jobs/
COPY utils/ /app/utils/

# Set environment variables
ENV AIRFLOW_HOME=/app
ENV AIRFLOW__CORE__LOAD_EXAMPLES=False

# Expose the webserver port
EXPOSE 8080

# Start the webserver
CMD ["airflow", "webserver"]