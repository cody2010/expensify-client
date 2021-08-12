from unittest.mock import MagicMock, patch
from ..expensify_client.client import ExpensifyClient

class ExpensifyClientUnitTestCase():

    def setUp(self):
        super(ExpensifyClientUnitTestCase, self).setUp()
        self.expensify_client = ExpensifyClient(username="TEST", password="TEST", sandbox=True)

    def test_get_report_download(self):
        self.skipTest('This test is meant for local debugging only')
        filters = {
            "startDate": "2020-01-01",
            "endDate": "2020-01-30"
        }
        download_file = self.expensify_client.get_report_download_file(filters, 'json', 'expensify_report_export_template.ftl')
        download = self.expensify_client.download_reports(download_file)

        self.assertEqual(1, 1)

    def test_get_reports(self):
        self.skipTest('This test is meant for local debugging only')
        parameters = {
            'filters': {
                "startDate": "2020-01-01",
                "endDate": "2020-01-30"
            },
            'report_parameters': ['reportName', 'accountEmail', 'reimbursed', 'status'],
            'transaction_parameters': ['created', 'modifiedCreated', 'modifiedAmount', 'amount',
                                       'merchant', 'modifiedMerchant']
        }

        reports = self.expensify_client.get_reports(parameters)
        self.assertEqual(1, 1)

    def test_create_report_ftl_template(self):
        report_parameters = ['reportName', 'submitter', 'accountEmail', 'reimbursed', 'status']
        transaction_parameters = ['modifiedAmount', 'modifiedCreated', 'amount']

        file = self.expensify_client.create_report_ftl_template(report_parameters, transaction_parameters)
        self.expensify_client.delete_report_ftl_template("ftl_template.ftl")
        self.assertEqual(1, 1)