import requests
import logging

# Configure logging
logging.basicConfig(filename='app_health.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

# URL to monitor
APP_URL = "http://www.google.com"

def Application_health_chceker():
    try:
        response = requests.get(APP_URL)
        if response.status_code == 200:
            message = f"Application is UP. Status Code: {response.status_code}"
            logging.info(message)
            print(message)
        else:
            message = f"Application is DOWN. Status Code: {response.status_code}"
            logging.warning(message)
            print(message)
    except requests.exceptions.RequestException as e:
        message = f"Application is DOWN. Error: {str(e)}"
        logging.error(message)
        print(message)

if __name__ == "__main__":
    Application_health_chceker()
