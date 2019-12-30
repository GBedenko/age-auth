# age-auth

AgeAuth - Application which offers two main interfaces:

* Scans a webpage using a Regular Expressions to see if keywords appear at the provided URL

* Captures a photo of the user via their webcam and then calls facial recognition software to determine their age

Both of these interfaces only run locally so that no data is passed to external APIs - to keep data secure and private

Google Chrome extension used to call these interfaces when needed (i.e. when age-restricted keywords are on the current webpage)

## Prerequisites

```console
sudo apt install python3

sudo apt install python3-pip

sudo pip3 install -r requirements.txt

sudo apt install git
```

## Setup

```console
git clone https://github.com/GBedenko/age-auth

cd age-auth
```

## Start Server

```console
./app.py
```
