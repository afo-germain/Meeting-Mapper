# Meeting Mapper


## Overview

The Meeting Mapper is a project that optimizes meetings between friends by facilitating planning and coordination via an interactive web application.

## Features

- User profile management:
- Dynamic mapping
- Matrix of origin and destinations
- Calculating the optimum location
- Route planning
- Real-time tracking
- ...

## Getting Started

To run this project locally, follow the instructions below.

### Prerequisites

Before you begin, make sure you have the following installed:

- [Python](https://www.python.org/) (>= 3.6)
- Code editor - preferably Vscode

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/afo-germain/Meeting-Mapper

2. Navigate to the project directory:
    ```bash
    cd Meeting-Mapper/API
3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv env
4. Activate the virtual environment:
- On Windows:
    ```bash
    .\env\Scripts\activate
- On MacOs:
    ```bash
    source env/bin/activate

5. Install dependencies:
   ```bash
   pip install -r requirements.txt

6. Finally run the Application
   ```bash
   uvicorn main:app --reload --host 127.0.0.1 --port 8000

### Usage
    Once the application is running, you can access at http://127.0.0.1:8000/docs
    for interactive documentation.

    Open Wep-App/index.html in browser
