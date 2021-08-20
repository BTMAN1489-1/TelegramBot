# TelegramBot

***This telegram bot works through a webhook using nginx reverse proxying and a free certificate from Let's Encrypt.***
## Tutorial
### Dependencies:
1. Get a telegram bot token from [BotFather](https://core.telegram.org/bots#3-how-do-i-create-a-bot);
2. Rent a linux-based virtual machine on a cloud server, for example [here](https://azure.microsoft.com/en-us);
3. Сonfigure your remote server (for example, configure http / https connections, shh connections and create your server domain name);
4. Install [docker](https://docs.docker.com/engine/install) and [docker-compose](https://docs.docker.com/compose/install) to your remote server;
5. Get a free [Let's Encrypt](https://letsencrypt.org/getting-started) certificate for the domain name of your remote server;

### First step:
  - Clone this repository to your remote server with the command `git clone https://github.com/BTMAN1489-1/TelegramBot.git`;
  - Go to the project folder with the command `cd TelegramBot`;

### Bot setup:
  - Go to folder `telegrambot` with command `cd telegrambot`;
    - Сreate a bot configuration file `.env` following the next example:
      ```.env
      API_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11    # your token should be here
      WEBHOOK_HOST=https://example.com                       # your domain name of remote server should be here
      ```
  - Go to the root of the project with the command `cd ..`;
 ### Nginx server setup:
  - Go to folder `nginx` with command `cd nginx`;
    - Open nginx config file `nginx.conf` with command `nano nginx.conf`;
      - Insert your domain name of the remote server instead of the 'example.com';
      - Save and exit;
  - Go to the root of the project with the command `cd ..`;

### Running docker containers:
  - Enter the command `docker-compose up`;

## Your bot is running!!!
