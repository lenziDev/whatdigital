# What Digital Trial Project


<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [What Digital Trial Project](#what-digital-trial-project)
- [Documentation](#documentation)
  - [Installation](#installation)
    - [Django](#django)
    - [React](#react)
  - [Build](#build)
  - [Test](#test)
  - [Deploy and Running the application](#deploy-and-running-the-application)
- [Limitations](#limitations)
- [Next Steps](#next-steps)

<!-- /code_chunk_output -->


# Documentation

## Installation

### Django
- Go to the project folder in `backend/whatdigital`
- Install dependencies: 
```
pip install -r requirements.txt
```
- Create database tables: 
```
python manage.py migrate
```
- Run the development server: 
```
python manage.py runserver
```
### React
- Go to the project folder in `frontend`
- Install dependencies: 
```
npm install
```
- Run the development server: 
```
npm start
```

## Build

## Test

The Django project uses pytest, so in the project folder you can run:

```
pytest
```

## Deploy and Running the application

# Limitations

- No authentication in the products backend endpoints. List products and update product check mark
- No pagination in the products list, limiting the total amount of products that can be added to the system
- The database in SQLite, if we need more performance we can change to Postgresql as it is recommended in Django documentation
- Product description limited to 255 characters

# Next Steps

- Update the interface of the product selection, this was not specified in the requirements and the final implementation was not good, didn't change because a lack of time in the 4 hours of test
- Create the authentication and CSRF verification for the list and update product endpoint in Django, and the required code for the frontend
- Extends the tests in the backend and creates new tests for the frontend. For this trial was omitted because of a lack of time
- Update the settings to take the keys from a `.env` file in the backend
