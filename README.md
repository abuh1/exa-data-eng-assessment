# FHIR Data ETL Pipeline

A pipeline to process FHIR data through ETL processes and load into a PostgreSQL database.  


### Prerequisites  

Before running the pipeline, ensure that you have the following prerequisites installed on your system:

- Python 3.x
- Docker (if using Docker Compose)

### 1) Running with pip

To run the pipeline using pip, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    $ git clone https://github.com/abuh1/exa-data-eng-assessment.git
    ```

2. Navigate to the project directory:

    ```bash
    $ cd exa-data-eng-assessment
    ```

3. Install dependencies using pip:

    ```bash
    $ pip install -r requirements.txt
    ```

4. Run the ETL pipeline:

    ```bash
    $ python src
    ```

    Alternatively, if you're on windows you can run the run.bat file:

   ```bash
    run.bat
    ```

### 2) Running with conda

To run the pipeline using conda, follow these steps:

1. Clone the repository to your local machine (if you haven't already):

    ```bash
    git clone https://github.com/your-username/fhir-data-etl-pipeline.git
    ```

2. Navigate to the project directory:

    ```bash
    cd fhir-data-etl-pipeline
    ```

3. Create a conda environment from the provided environment file:

    ```bash
    conda env create -f condaenv.yml
    ```

4. Activate the conda environment:

    ```bash
    conda activate fhir-etl
    ```

5. Run the ETL pipeline:

    ```bash
    python etl_pipeline.py
    ```

### 3) Running with Docker Compose

To run the pipeline using Docker Compose, follow these steps:

1. Clone the repository to your local machine (if you haven't already):

    ```bash
    git clone https://github.com/your-username/fhir-data-etl-pipeline.git
    ```

2. Navigate to the project directory:

    ```bash
    cd fhir-data-etl-pipeline
    ```

3. Run Docker Compose to build and start the containers:

    ```bash
    docker-compose up
    ```

## Contributors

- John Doe (@johndoe)
- Jane Smith (@janesmith)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to the FHIR community and the contributors to the libraries and tools used in this project.
