# FHIR Data ETL Pipeline

A pipeline to process FHIR data through ETL processes and load into a PostgreSQL database.  


### Prerequisites  

Before running the pipeline, ensure that you have the following prerequisites installed on your system:

- Python 3.x
- Docker (if using Docker Compose)

## Running using pip

After cloning the repo, be sure to replace the database credentials inside src/config.py inside the postgresql_credentials dictionary to your own.
Make sure to change the PATH_TO_DATA in the same config.py file to your path to the data.

- Clone the repository to your local machine:

    ```bash
    $ git clone https://github.com/abuh1/exa-data-eng-assessment.git
    ```

- Navigate to the project directory:

    ```bash
    $ cd exa-data-eng-assessment
    ```

- Install dependencies using pip:

    ```bash
    $ pip install -r requirements.txt
    ```

- Run the ETL pipeline:

    ```bash
    $ python src
    ```

  Alternatively, if you're on windows you can run the run.bat file:

   ```bash
    run.bat
    ```

## 2) Running with conda

After cloning the repo, be sure to replace the database credentials inside src/config.py inside the postgresql_credentials dictionary to your own.
Make sure to change the PATH_TO_DATA in the same config.py file to your path to the data.
Ensure you have conda installed before following the steps:

- Clone the repository to your local machine (if you haven't already):

    ```bash
    $ git clone https://github.com/abuh1/exa-data-eng-assessment.git
    ```

- Navigate to the project directory:

    ```bash
    $ cd exa-data-eng-assessment
    ```

- Create a conda environment from the provided environment file. Type the name of your desired environment in place of <env>:

    ```bash
    $ conda create --name <env> --file environment.yml
    ```

- Activate the conda environment using your environment name:

    ```bash
    $ conda activate <env>
    ```

- Run the ETL pipeline:

    ```bash
    $ python src
    ```

## 3) Running with Docker Compose

Replace the following in the docker-compose.yml file: 'your/path/to/data' with your path to your own data.

- Navigate to the directory containing the repo and run:

    ```bash
    $ docker-compose up
    ```

- To take down the containers use CTRL+C to exit command line and then enter:

    ```bash
    $ docker-compose down
    ```

- To delete volumes

    ```bash
    $ docker-compose down --volumes
    ```

  ## Without docker

    ![TerminalSS](/demo/program.png)  

  ## With docker-compose

    ![Dockercompose](/demo/docker-compose.png)
  
  ## Database
    ![Database](/demo/database.png)
