# L3HARRIS TASK

## TABLE OF CONTENT 
* [Introduction](#introduction)
* [Main Technologies used](#main-technologies-used)
* [Task](#task)     
* [Installation](#installation)
* [Haversine Formula](#installation)
* [Design Approach](#design-approach)
* [Command Line Inteface](#command-line-interface)
* [Django interface method 1](#django-interface-method-1)
* [Django interface method21](#django-interface-method-2)
* [Flask Inteface](#flask-interface)
* [API Endpoint](#api-endpoint)
* [Output Format](#output-format)  
* [Error Handling](#error-handling)
* [Testing](#testing)


## INTRODUCTION 

This section provides details on the technology and methodology used for the L3HARRIS task.

## TASK

Write a program that accepts a decimal logitude and latitude location and displays the closest airport from a csv data file provided.


## MAIN TECHNOLOGIES USED

* Python (v3.9.13)
* pandas package for distance computations
* Django for user interface and storing airport details


## INSTALLATION

1. create virtual environment using :  ``` python -m venv .venv ```
2. Activate virtual environment: ``` .\.venv\Scripts\activate ```
3. Install all libraries: ``` pip install -r requirements.txt ```
4. When using method 3 run the following command to store airport into model:

        ``` python manage.py makemigrations ```

        ``` python manage.py migrate ```

        ``` python manage.py store_airport ```


## HAVERSINE FORMULA

The shortest distance calculation was done using the Haversine Formula:

    a = sin²(φB - φA/2) + cos φA * cos φB * sin²(λB - λA/2)

    c = 2 * atan2( √a, √(1−a) )

    d = R ⋅ c

The python function executing the formula can be found [here](api/utils.py)


## DESIGN APPROACH

Three approaches were used to obtain nearest airport:
1. Command line interface. 
2. Django with input form interface using CSV file to create dataframe.
3. Django with input form interface using model data to create dataframe.


## COMMAND LINE INTERFACE

This interface provides a mean to obtain nearest airport by running the command ``` python main.py ```. 

This method creates a dataframe directy from csv file.


## DJANGO INTERFACE METHOD 1

This method provides a form interface to input latitude and longitude and renders the results to the same page in a tabular format```

The dataframe is created directy from csv file.

- Command to un Django Locally : ``` python manage.py runserver ```

![document](docs/image1.png)


## DJANGO INTERFACE METHOD 2

This method provides a form interface to input latitude and longitude and output's the response in json format.

This method creates a dataframe from the Django Model and requires the following command to run inorder to store the airport details into the model.

    ``` python manage.py store_airport ```

- Command to un Django Locally : ``` python manage.py runserver ```

- e.g output:
  
        {"input_latitude": 52.489471, "input_longitude": -1.898575, "airport": "BIRMINGHAM", "latitude": 52.453856, "longitude": -1.748028, "icao_code": "EGBB", "distance": "17.202 km"}    


## OUTPUT FORMAT

The output format includes the following fields:

- input latitude
- input longitude
- nearest airport name
- latitude of airport
- longitude of airport
- icao code
- distance

## ERROR HANDLING

For the command line interface, a basic while loop was used to ensure the input were of float type.

For the Django app, input error was handled using django forms.

### UNIT TESTING

Unit testing was perfommed using Python's unittest and Django Testcase. 

The test can be run with the following commands:

     ``` python unitest.py ```

     ``` python manage.py test  ```

The following parameters were checked:

1. Output format
2. Output data: airport name, distance

Test data for CITY airport was used.
