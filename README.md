# TheFabricTask

## Preparation

Copy values of the file `.env.sample` to `.env`

## Build & run project

```shell
docker compose up --build
```

## Usage

### Registration

First of all, register a new user:

```shell
curl -X POST http://127.0.0.1:8000/auth/users/ \
-H "Content-Type: application/json" \
-d '{
  "username": "newuser",
  "name": "John Doe",
  "password": "secretpassword"
}'
```

> Note: As a response you will receive token, that you need to **SAVE**.


Response:
```json
{
  "token": "your-authorization-token"
}
```

### Generating token for telegram bot

In order to receive messages from telegram bot, you need to bind your account with 
telegram account. This can be done with token, that you need to generate with this request:

```shell

curl http://127.0.0.1:8000/bot/generate-token/ \
-H "Content-Type: application/json" \
-H "Authorization: Token <your-authorization-token>"
```

> Note: As per this version of api, each user can obtain only 1 token. After generating a new token, you won't be able
> to change it

### Binding Token to your chat

In order to bind newly generated token to a chat, you need to send message to the <a href="https://t.me/TheFactoryTaskBot">bot</a>:

```text
register <your-generated-token>
```

> Note: you need to send it as a plain text, no slashes, **just text**.

If you did everything correctly, you will receive `Binded your token to this chat!` message.

### Sending messages to API and receiving via bot

Request:

```shell
curl -X POST http://127.0.0.1:8000/bot/send/ \
-H "Content-Type: application/json" \
-H "Authorization: Token <your-authorization-token>" \
-d '{
  "message": "Ayo!"
}'
```

### History of your messages

In order to see all the messages you sent, make request:

```shell
curl -X POST http://127.0.0.1:8000/bot/messages/me/ \
-H "Content-Type: application/json" \
-H "Authorization: Token <your-authorization-token>"
```