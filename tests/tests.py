import logging
import json
from datetime import date

from handlers import contacts_handler, timetable_handler, tutors_info_handler, utils_handler
from config import *


class BotTester:
    
    @staticmethod
    def _run_test(command: str, args: list) -> str:
        
        # INSERT YOUR CODE

        return obtained_response


    @staticmethod
    def _load_tests(input_file_path) -> dict:
        
        # INSERT YOUR CODE

        return tests
    
    
    @staticmethod
    def run_tests(test_file_path: str) -> None:

        # INSERT YOUR CODE


if __name__ == "__main__":
    
    test_file_path = os.path.join(PROJECT_DIR, "tests/tests_data/test_contacts.json")
    
    BotTester.run_tests(test_file_path)
