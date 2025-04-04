import requests
import csv

def check_urls_from_csv(file_path):
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            # Skip the header row
            next(reader)
            for row in reader:
                if row and row[0].strip():  # Check if row exists and isn't empty
                    url = row[0].strip()
                    try:
                        response = requests.get(url, timeout=5)
                        print(f"({response.status_code}) {url}")
                    except requests.exceptions.Timeout:
                        print(f"(TIMEOUT) {url} - The server took too long to respond.")
                    except requests.exceptions.ConnectionError:
                        print(f"(ERROR) {url} - The website is unreachable or does not exist.")
                    except requests.exceptions.RequestException as e:
                        print(f"(ERROR) {url} - {e}")
    except FileNotFoundError:
        print("Error: CSV file not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Update with your CSV filename
csv_file_path = "Task 2 - Intern.csv"
check_urls_from_csv(csv_file_path)

