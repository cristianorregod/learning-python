# Basic web server example

This project is a learning exercise focused on building a simple web application using Python and the FastAPI framework. It showcases how to create HTTP endpoints to serve JSON data and HTML content. Through this project, you'll learn about module import, framework usage, decorators, routing, function definition, response types, conditional execution, and function calls in Python. It provides hands-on experience in building web APIs and handling different types of responses, serving as an educational resource for those interested in web development with Python.

## What i learned

-   **Module Import**: The store module is imported, indicating that there is a separate Python file (store.py) that contains code that will be used in this script.

-   **Framework Usage**: The FastAPI framework is used to create a web application. This demonstrates the use of a third-party library to build web APIs in Python.

-   **Decorators**: @app.get('/') and @app.get('/html') are decorators used to define HTTP GET endpoints in FastAPI. They associate the get_users() and get_html_content() functions with the respective routes.

-   **Routing**: The @app.get() decorators define routes for handling HTTP GET requests with specific URLs (/ and /html).

-   **Function Definition**: The get_users() and get_html_content() functions are defined to handle HTTP GET requests and return JSON data and HTML content, respectively.

-   **Response Types**: The HTMLResponse class from fastapi.responses is used to specify that the response of the /html endpoint should be in HTML format.

-   **Conditional Execution**: The if **name** == '**main**': block ensures that the run() function is executed only when the script is run directly (not imported as a module).

-   **Function Call**: The run() function is called to execute the code that retrieves store categories from the store module.

## Usage

To execute this pice of code you only need to clone this project and then in your terminal run the main file --> web-server/main.py

```sh
# clone de repo
git clone https://github.com/cristianorregodev/learning-python.git

#open the project
cd learning-python/web-server

#Create the virtual env
python3 -m venv env

#Run the virtual env
source env/bin/activate

#Install dependencies
pip3 install -r requirements.txt

#run the application
python3 main.py

```
