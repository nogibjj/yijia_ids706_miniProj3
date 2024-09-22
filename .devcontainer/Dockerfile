# Use the official Python image
FROM python:3

# Set the working directory in the container
WORKDIR /workspace

# Copy all files from the parent directory to the working directory
COPY ../* /workspace/

# Install dependencies
RUN pip install --no-cache-dir -r /workspace/requirements.txt

# Install make utility
RUN apt-get update && apt-get install -y make && \
    rm -rf /var/lib/apt/lists/*

# Set the default command to run all targets defined in Makefile
# CMD ["make", "all"]
