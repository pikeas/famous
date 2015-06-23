FROM aris/iojs:2.3.0
MAINTAINER Aris Pikeas <aris@pike.as>

ENV PATH /app/node_modules/.bin:$PATH

WORKDIR /app

COPY package.json ./
RUN npm install

COPY . ./

EXPOSE 5001
CMD ["coffee", "src/server.coffee"]
