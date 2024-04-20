# OpenAPITestImpl - Setup Guide

This guide walks you through setting up the Python project for the Talk2Note backend application, named OpenAPITestImpl. 

### Setting up Python Virtual Environment and .env File

##### Creating Python Virtual Environment (venv)


1. Open Command Prompt (cmd) or PowerShell.
2. Navigate to your project directory using `cd` command.
3. Create Venv
    - Create (Kernel): `python3 -m venv venv` (**Requires Python 3.x**)
    - Create (Windows): `python -m venv venv`
4. Activate
    - Activate (Kernel): `source venv/bin/activate`
    - Activate (Windows): `venv/Scripts/activate`
5. Deactivate: `deactivate`

**It's important to deactivate the virtual environment when you're finished to avoid conflicts with other projects that may have different dependency requirements.**

### Creating .env File

1. In your project directory, create a new file named `.env`.
2. Open in a text editor.
3. Add environment variables in format `KEY=VALUE`.
For example: `OPENAI_API_KEY=my-special-key`
4. Save.

### Installing Packages

After activating the environment, install the packages listed in the "requirements.txt" file. This file specifies the external libraries your project needs to run.

**To install the required packages, run the following command after activating the virtual environment:**

`python -m pip install -r requirements.txt`

### Running Project

To run project need to call main file inside source (/src/main.py)
> after activating virtual environment ~

`python src/main.py`


### Configuration

Project configuration is handled from the OpenAI Roles configuration JSON file located at `${PROJECT_ROOT}/src/data/note-taker.json`.

**Make sure to replace `${PROJECT_ROOT}` with the actual root directory of your project.**

## Congratulations

Congratulations you've completed all requirements. You can now test the project freely !.