# Amazon Web Scraper Project

## Overview

The Amazon Web Scraper Project is designed to track the daily price of the iPhone 15 on Amazon. It sends an email notification when the price drops below $1400. This project uses Python for web scraping, data analytics, and visualization.

## Features

- **Daily Price Tracking**: Scrapes the price of the iPhone 15 from Amazon every day.
- **Email Notifications**: Sends an email alert when the price drops below $1400.
- **Data Analytics**: Analyzes the price trends over time.
- **Data Visualization**: Visualizes the price trends using graphs.

## Libraries Used

- `pandas`: For data manipulation and analysis.
- `BeautifulSoup`: For web scraping.
- `smtplib`: For sending email notifications.
- `requests`: For making HTTP requests to fetch the web page content.
- `time` and `datetime`: For scheduling and monitoring daily scraping tasks.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/amazon-web-scraper.git
    cd amazon-web-scraper
    ```

2. Install the required libraries:
    ```bash
    pip install pandas beautifulsoup4 requests
    ```

## Usage

1. **Set up email configuration**:
    - Open `config.py` and add your email credentials and recipient email address:
    ```python
    EMAIL_ADDRESS = 'tkt@njit.edu'
    EMAIL_PASSWORD = 'CCCCCCCCC
    RECIPIENT_EMAIL = 'tkt@njit.edu'
    ```

2. **Run the scraper**:
    ```bash
    python scraper.py
    ```

3. **Analyze and visualize the data**:
    - The script saves the scraped data to a CSV file named `AmazonWebScraperProject.csv`. You can run the following script to analyze and visualize the data:
    


## How It Works

1. **Scraping the Price**:
    - The `scraper.py` script uses the `requests` library to fetch the HTML content of the Amazon product page.
    - The `BeautifulSoup` library is used to parse the HTML and extract the price of the iPhone 15.

2. **Sending Email Notifications**:
    - If the scraped price is below $1400, the `smtplib` library is used to send an email notification to the specified recipient.

3. **Data Analytics and Visualization**:
    - The `analyze.py` script uses the `pandas` library to read the price data from the CSV file and perform data analysis.
    - The `matplotlib` library is used to visualize the price trends over time.

4. **Scheduling Daily Scraping**:
    - The `time` and `datetime` libraries are used to schedule the scraper to run daily, ensuring up-to-date price tracking.

## Future Improvements

- Add support for tracking multiple products.
- Implement a database to store the price data.
- Enhance the email notification system to include price trends and graphs.

## Contributing

If you would like to contribute to this project, please fork the repository and create a pull request with your changes.


## Contact

If you have any questions or suggestions, feel free to reach out to me at tkt@njit.edu

---

Thank you for using the Amazon Web Scraper Project!
