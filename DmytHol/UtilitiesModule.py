from PIL import Image
from io import BytesIO
import os
import json
import csv

class UtilitiesModule:
    # Function to capture a screenshot and save it with the provided file name.
    def capture_screenshot(self, file_name):
        try:
            screenshot = self.driver.get_screenshot_as_png()
            screenshot_path = os.path.join(os.getcwd(), file_name)
            with open(screenshot_path, 'wb') as f:
                f.write(screenshot)
            return screenshot_path
        except Exception as e:
            print(f"Failed to capture screenshot: {e}")
            return None

    # Function to read and parse data from a file (supports JSON and CSV formats).
    def read_data(self, file_path):
        try:
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension == '.json':
                with open(file_path, 'r') as json_file:
                    data = json.load(json_file)
            elif file_extension == '.csv':
                with open(file_path, 'r') as csv_file:
                    reader = csv.DictReader(csv_file)
                    data = [row for row in reader]
            else:
                print(f"Unsupported file format: {file_extension}")
                return None
            return data
        except Exception as e:
            print(f"Failed to read data from file: {e}")
            return None