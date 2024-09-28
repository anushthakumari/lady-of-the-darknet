# Lady of the Darknet

## Description

**"Lady of the Darknet"** is a Flask application that monitors dark web data leaks, uncovering compromised information and the groups behind these breaches.

## Prerequisites

To run this project, you must have:

- Python 3.x
- Tor Browser (must be running)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/anushthakumari/lady-of-the-darknet.git
   cd lady-of-the-darknet
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv  # Create the virtual environment
   ```

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

3. Install the required packages using `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Ensure that the Tor Browser is running.

2. Execute the scraper file to start scraping data:

   ```bash
   python scraper.py
   ```

3. Then, execute the main file:

   ```bash
   python main.py
   ```

4. Open your web browser and navigate to `http://127.0.0.1:5000` to access the application.

## License

This project is licensed under the FFTU (Feel Free To Use) License. See the LICENSE file for more details.

## Acknowledgements

- Flask for web development.
- Selectolax for efficient HTML parsing.
