FROM node:20.18-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

# RUN npm run build

EXPOSE 3000

RUN npm run start --host 0.0.0.0 --port 3000