# Async Python
These exersice files are to be used in conjuction with the course "Async Python" on LinkedIn Learning

## Easy setup with gitpod(cloud workspace)
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#/https://github.com/LinkedInLearning/async-python-foundations-applied-concepts-2422322)

These exersice files are to be used in conjuction with the course "Async Python" on  [LinkedIn Learning](https://www.linkedin.com/learning)

## Local setup
## Downloads
* Visit [python.org](https://www.python.org/) and download Python for your operating system.
* Visit [redis.io](https://redis.io/download) and download Redis for your operating system.

## Setting up a vertual environment.
1. Create a virtual environmet with the following command:
   ```bash
   python3 -m venv venv
   ```
1. Activate the vertual environment:
   1. Linux and Mac
   ```bash
   source venv/bin/activate
   ```
   2. Windows
   ```bash
   venv\Scripts\activate
   ```
   > :warning: *If you encounter an error using Windows PowerShell, try opening another shell with the "Run as Administrator" option.*
1. Install the required packages
   ```
   pip install -r requirements.txt
   ```

## Every time you start a terminal session
1. Navigate to the course directory

1. Activate the vertual environment:
   1. Linux and Mac
   ```bash
   source venv/bin/activate
   ```
   2. Windows
   ```bash
   venv\Scripts\activate
   ```
 
 
## Running a single exercise file.
> :warning: *Make sure that you have set up your environment according to the instructions above*

1. Python
   ```bash
   python CH_01_04_end.py
   ```
1. Starting redis(in seperate terminal)
   ```bash
   redis-server
   ```

