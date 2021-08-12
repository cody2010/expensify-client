# expensify-client
A python wrapper for Expensifys API.
Currently supports
- Getting reports

## How Expensify Works
Expensify's API is a little clunky and requires the following steps:
1. Generate a .ftl template file that specifies the report level and transaction
level parameters you want to receive, as well as the formatting in which you
want it
2. Send a request with specific filters as well as the template to Expensify's
server. Expensify will intake that information and return a file name. (This is
their Report Exporter call)
3. Send a second request to expensify to download the returned file name. (This is
their Downloader call)

## How this package works
This package provides a client class that intakes 3 parameters: filters, report 
parameters, transaction parameters. It generates the ftl template from your parameters and returns a json dictionary object.

### Filters
Pass in a dictionary object much like Expensify's documentation provides:
```
"filter":{
            "startDate": "2016-01-01",
            "endDate": "2016-10-10",
            "domain": "example.com",
            "feed": "export_all_feeds",
            "type": "Unreported",
            "async": false
        }
```

### Report and Transaction Parameters
These are lists of Expensify defined parameters that can be viewed on their documentation https://integrations.expensify.com/Integration-Server/doc/export_report_template.html. 

## Methods

### get_reports(filters: dict, report_parameters: list, transaction_parameters: list)

Returns a json dictionary as follows:
```
{
    reportID: {
        reportParameter1: value,
        reportParameter2: value,
        ...
        transactions: [
            {
                transactionID: xyz,
                transactionParameter1: value,
                transactionParameter2: value,
                ...
            }
        ]
    }
}
```
## Intended Usage
This package is intended as a base client class that you can inherit in your own custom class. Use the base methods to pull out formatted json which you can then manipulate as needed.

We don't include a configuration format, simply plug in your expensify username and password into the ExpensifyClient and handle your credentials however you usually set them.

## Example Code
```
from expensify_client import ExpensifyClient

class CustomExpensifyClient(ExpensifyClient):
        def __init__(self):
            username = YOUR_USERNAME
            password = YOUR_PASSWORD

        super(CustomExpensifyClient, self).__init__(username, password)

my_client = CustomExpensifyClient()
reports = my_client.get_reports(filters, report_parameters, transaction_parameters)
```

## Todo
1. Provide more hooks to replace characters on download. We have the ability to specify characters to replace, but haven't put the hook into the get_reports function. See the replace_ftl_characters() method.
2. Provide sandbox instance support. We pass a sandbox parameter into the client, but currently it's unused. 