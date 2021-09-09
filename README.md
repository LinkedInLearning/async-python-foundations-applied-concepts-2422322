# Async Python Foundations: Applied Concepts
This is the repository for the LinkedIn Learning course Async Python Foundations: Applied Concepts. The full course is available from [LinkedIn Learning][lil-course-url].

![Async Python Foundations: Applied Concepts][lil-thumbnail-url] 

If you were cooking a multicourse meal, would you prep one thing at a time? Put bread in the oven, wait. Warm the soup on the stove, wait. Then the main course. Wouldn’t it be more efficient to spend time prepping other food instead of waiting on tasks that don’t need your immediate attention? In the same way that having multiple things happen at the same time leads to faster meal prep, having multiple things happen in Python—or using an asynchronous approach—can be leveraged to boost application performance and make your Python programs extremely efficient. In this course, Ronnie Sheer gives you the tools to use async Python to solve real-world problems, gain familiarity with the async Python ecosystem, complete challenges with working examples, and become a more attractive candidate for engineering positions. If you’re an experienced Python user looking to take async Python from theory to practice, check out this hands-on course.

## Easy setup with Gitpod (cloud workspace).
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#/https://github.com/LinkedInLearning/async-python-foundations-applied-concepts-2422322)

## Local setup
## Downloads
* Visit [python.org](https://www.python.org/) and download Python for your operating system.
* Visit [redis.io](https://redis.io/download) and download Redis for your operating system.

## Setting up a virtual environment
1. Create a virtual environment with the following command:
   ```bash
   python3 -m venv venv
   ```
1. Activate the virtual environment.
   1. Linux and Mac
   ```bash
   source venv/bin/activate
   ```
   2. Windows
   ```bash
   venv\Scripts\activate
   ```
   > :warning: *If you encounter an error using Windows PowerShell, try opening another shell with the "Run as Administrator" option.*
1. Install the required packages.
   ```
   pip install -r requirements.txt
   ```

## Every time you start a terminal session
1. Navigate to the course directory.

1. Activate the virtual environment.
   1. Linux and Mac
   ```bash
   source venv/bin/activate
   ```
   2. Windows
   ```bash
   venv\Scripts\activate
   ```
 
## Running a single exercise file
> :warning: *Make sure that you have set up your environment according to the instructions above.*

1. Python
   ```bash
   python CH_01_04_end.py
   ```
1. Starting redis(in separate terminal)
   ```bash
   redis-server
   ```
   
   
### Instructor

Ronnie Sheer                            

Check out my other courses on [LinkedIn Learning](https://www.linkedin.com/learning/instructors/ronnie-sheer).

[lil-course-url]: https://www.linkedin.com/learning/async-python-foundations-applied-concepts
[lil-thumbnail-url]: https://cdn.lynda.com/course/2422322/2422322-1630605594091-16x9.jpg

