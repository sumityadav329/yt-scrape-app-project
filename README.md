# YouTube Data Scraper

YouTube Data Scraper is a Flask web application that allows users to scrape video data from a YouTube channel and export it to a CSV file. The application uses Selenium for web scraping and Flask for the web framework.

## Features

- Scrape video titles, links, thumbnails, views, and time of posting from a specified YouTube channel.
- Display the scraped data in a user-friendly format on a result page.
- Allow users to download the scraped data as a CSV file.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Selenium
- ChromeDriver (compatible with your Chrome browser version)

### Installation

1. Clone the repository:


   git clone https://github.com/sumityadav329/yt-scrape-app-project.git
   

2. Install dependencies:

   pip install -r requirements.txt
   

3. Download and install ChromeDriver: [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/)

4. Update the `chromedriver.exe` path in `app.py`:

   
   service = Service(executable_path='./chromedriver.exe')
   

## Contributing

If you would like to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Flask and Selenium communities for their excellent documentation.
