[![deploy workflow](https://github.com/nindowell/django-github-cicd/actions/workflows/deploy-services.yml/badge.svg)](https://github.com/nindowell/django-github-cicd/actions/workflows/deploy-services.yml)
### Description
This is my template repository for future django projects with set up django custom user application (password change and reset with an email confirmation), crispy forms for bootstrap and Github Actions CI/CD workflow example.
 - Live version https://user-ready.nindo.online (works on self-hosted runner)

### For deployment on a server
#### Prerequisite
For the Let's Encrypt HTTP challenge you will need:

- A publicly accessible host allowing connections on port `80` & `443` with docker & docker-compose installed. A virtual machine in any cloud provider can be used as a host.
- A DNS record with the domain you want to expose pointing to this host.

#### Steps on a server
1. Clone the repository on your host and go to the directory:
```console
git clone https://github.com/nindowell/django-github-cicd
cd django-github-cicd
```

2. Run, specifying your domain in .env file MY_DOMAIN=your.domain.com:
```console
docker compose -f docker-compose.yml -f docker-compose.tls.yml up -d
```

It will take a few seconds to start the database, migrate, collect static files, and obtain a Let's Encrypt certificate. So wait a little and open https://your.domain.com in your browser. Your server is ready to work

> Don't worry about renewing the Let's Encrypt certificate, it will happen automatically.

### To clean up
The command below will stop all containers, remove them and their images.
```console
docker compose down --remove-orphans --rmi local
```
In this workflow i'm using this:
```console
docker compose down --rmi local
```

> This repository was adapted from [github amerkurev's django template](https://github.com/amerkurev/django-docker-template/) repository and modified with Github Actions CI/CD workflow setup