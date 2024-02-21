# Project Smarter-1-QA



## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Python 3.7+ (ideally 3.11)
- pip (Python package installer)

### Installing

A step-by-step series of examples that tell you how to get a development environment running:

1. Clone the repository:
   ```sh
   git clone https://github.com/Smarter-Sorting/smarter1-qa.git
 
### Setup

1. Install required packages:
  ```SH
  pip install -r requirements.txt
```

### Run tests 

Optional-prerequisite (create virtual env - this step is recommended, but not mandatory): 
````
python3 -m venv venv
source venv/bin/activate
````


1. To run a specific test file:
```
CLASSIFICATION=IS_OTC_DRUG pytest tests/ --html=report.html --self-contained-html
```


Note: each time new package is added please include it into requirements.txt 
````
pip3 freeze > requirements.txt
````
