
# FROM python:3.10.4

# WORKDIR /Desktop/Diseases Detection system

# COPY requirements.txt .

# RUN pip install --no-cache-dir -r requirements.txt

# COPY .trained.h5 /Desktop/Diseases Detection system/

# CMD [ "python", "app.py" ]
FROM python:3.10.4

WORKDIR /Desktop/DiseaseDetection

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "app.py" ]

