# 1. Use an official Python runtime as a parent image
# (Think of this as the "OS" inside the box)
FROM python:3.9-slim

# 2. Set the working directory in the container
WORKDIR /app

# 3. Copy the requirements file into the container
COPY requirements.txt .

# 4. Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the current directory contents into the container
COPY . .

# 6. Run the application when the container launches
CMD ["python", "main.py"]
