FROM aris/python3:3.4.3-1
MAINTAINER Aris Pikeas <aris@pike.as>

ENV PATH /root/.local/bin:$PATH
ENV PYTHONPATH /app/src

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . ./

EXPOSE 5000
CMD ["python3", "-m", "server"]
