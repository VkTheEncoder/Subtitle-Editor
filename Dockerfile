# Use a slim Python base
FROM python:3.10-slim

# set a working directory
WORKDIR /app

# copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy our bot code
COPY . .

# expose the port Koyeb will route to (default 8080)
ENV PORT 8080
EXPOSE 8080

# start the bot
CMD ["python", "main.py"]
