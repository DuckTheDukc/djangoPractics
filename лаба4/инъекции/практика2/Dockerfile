FROM node:23.2.0-bullseye

# Установите необходимые зависимости
RUN apt-get update && apt-get install -y \
    libc6 \
    && rm -rf /var/lib/apt/lists/*

# Установите ваше приложение
WORKDIR /app
COPY . .

# Установите npm registry
RUN npm config set registry http://registry.npmjs.org/

# Установите зависимости
RUN npm install

# Запустите ваше приложение
CMD ["npm", "run", "build"]
