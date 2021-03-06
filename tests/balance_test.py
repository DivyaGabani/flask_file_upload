"""This test csv file test"""
import csv
from app.db.models import User


def test_csv_file_transaction(client, add_user, application):
    """This test csv file is created or not """
    with application.app_context():
        user = User('dummy1@test.com', 'abcd1234')
        filepath = 'tests/transaction1.csv'
        with open(filepath) as file:
            csv_read = csv.DictReader(file)
            for row in csv_read:
                test_csv = row
            assert test_csv == {'AMOUNT': '2000', 'TYPE': 'CREDIT'}