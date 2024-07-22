# Population charts generator by Country

This Python project focuses on data analysis and visualization using data from a CSV file. It reads data related to world population percentages by continent, filters out countries in South America, and then generates both pie and bar charts to visualize the population distribution. Additionally, it allows users to input a specific country and provides information about its population. Through modules and functions, it showcases various Python concepts such as file handling, data manipulation, filtering, mapping, visualization, and user interaction.

## What i learned

-   **Modules and Packages**: The code imports and utilizes modules and functions from the files utils.py, read_csv.py, and charts.py. Learning how to organize code into modules and packages can help structure larger projects more effectively.

-   **Reading CSV Files**: The code uses the read_csv.read_csv() function to read data from a CSV file named 'data.csv'. Learning to read and manipulate data from CSV files is an important skill in Python, especially for working with datasets.

-   **Data Filtering**: The filter() function is used along with a lambda expression to filter the data and select only those belonging to the continent 'South America'. Learning to filter and process data according to certain criteria is essential for data analysis in Python.

-   **Data Mapping**: The map() function and lambda expressions are used to extract lists of countries and population percentages from the filtered dataset. Learning to map and transform data from one form to another is an important skill in data analysis and processing.

-   **Data Visualization**: The charts.generate_pie_chart() function is used to generate a pie chart and charts.generate_bar_chart() to generate a bar chart based on the filtered and mapped data. Learning to visualize data effectively is crucial for communicating information clearly and understandably.

-   **User Input**: The input() function is used to prompt the user to enter a country. Learning to handle user input and take actions based on it is a common skill in many interactive programs.

## Usage

We can run this basic example by executing the main.py file located in `population-charts/main.py`.

```sh
# clone de repo
git clone https://github.com/cristianorregodev/learning-python.git

#open the project
cd learning-python/population-charts

#Create the virtual env
python3 -m venv env

#Run the virtual env
source env/bin/activate

#Install dependencies
pip3 install -r requirements.txt

#run the application
python3 main.py

```

Then you only have to visualize the output file generated in --> `imgs`
