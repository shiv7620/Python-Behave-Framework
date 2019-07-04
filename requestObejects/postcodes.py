from utilities.GlobalVariables import envConfig
import requests

from utilities.consoleReporter import ConsolePrint, Status


class PostCodes:

    baseURL = envConfig['apiBaseURL']

    def getPostcodeSuggestions(self, partialPostCode):

        # Defining API endpoint and sending request
        endpoint = self.baseURL + '/postcodes/' + partialPostCode + '/autocomplete'
        response = requests.get(url=endpoint)

        # Verifying request status
        assert response.status_code is 200, "Postcodes autocomplete - Verify if request is successful"
        ConsolePrint(Status.Info, endpoint, response.text)

        # Verifying request json context
        data = response.json()
        ConsolePrint(Status.Info,"Api result =", data['result'])

        assert data['result'] is not None, "Postcodes autocomplete - Verify if list is returned"

        # Returning some json node
        return data['result']


    def getPostcodeDetails(self, postCode):

        # Defining API endpoint and sending request
        endpoint = self.baseURL + '/postcodes/' + postCode
        response = requests.get(url=endpoint)

        # Verifying request status
        assert response.status_code is 200, "Postcodes autocomplete - request successful"
        ConsolePrint(Status.Info, endpoint, response.text)

        return response.json()


    def getPostcodeValidated(self, postCode):

        # Defining API endpoint and sending request
        endpoint = self.baseURL + '/postcodes/' + postCode + '/validate'
        response = requests.get(url=endpoint)

        # Verifying request status
        assert response.status_code is 200, "Postcodes autocomplete - request successful"
        ConsolePrint(Status.Info, endpoint, response.text)


        data = response.json()
        result = data['result']

        assert data['result'] is True, "Postcodes autocomplete - request successful"

        return True


    def postRandomPostCode(self, payload):

        endpoint = self.baseURL + '/postcodes'

        # To be loaded from template file or some other API output
        payload = {"postcodes": ["OX49 5NU", "M32 0JG", "NE30 1DP"]}

        response = requests.post(url=endpoint, json=payload)

        ConsolePrint(Status.Info, endpoint, response.status_code)
        ConsolePrint(Status.Info, endpoint, response.text)

        assert response.status_code is 200, "Postcodes autocomplete - request successful"

        data = response.json()

        # print(data['result'][0]['result']['postcode'])
        print(data['result'][0]['query'])
        # ConsolePrint(Status.Info, "PostCode =", data['result']['postcode'])

