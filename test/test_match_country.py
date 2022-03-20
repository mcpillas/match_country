# Import libraries
import requests
import pytest

# Global constants
BASE = "http://127.0.0.1:5000/"
STATUS_CODE = [200, 400, 404]
MESSAGES = ['Country ISO code is not valid...',
			"{'iso': 'Country ISO code required'}",
			"{'countries': 'Countries to compare with are required'}"]
# Valid requests
req_1 = {"iso": "svk",
	     "countries": [
             "iran",
             "Slowakei",
             "Vatikan",
             "Slovaška",
             "Szlovákia",
             "Belgrade",
             "España",
             "Nizozemsko"
	        ]}

req_2 = {"iso": "ECU",
	     "countries": [
             "조선",
             "Slowakei",
             "ඉක්වදෝරය",
             "Vatikan",
             "Slovaška",
             "Szlovákia",
             "에콰도르",
             "España",
             "South Korea",
             "Ekvádor"
	        ]}

# No matches
req_3 = {"iso": "jpn", "countries": ["조선"]}
# Invalid requests
# Empty ISO field
req_4 = {"iso": [], "countries": ["조선"]}
# Empty Countries field
req_5 = {"iso": "jpn", "countries": []}
# Empty ISO and Countries field
req_6 = {"iso": [],"countries": []}
# Invalid country ISO code
req_7 = {"iso": "jp", "countries": ["조선"]}

class TestCountryMatch:

	@staticmethod
	def compare_list(l1, l2):
		status = True if l1.sort() == l2.sort() else False
		return status

	def test_valid_requests(self):
		# Test request 1
		response = requests.post(BASE + "match_country", req_1)
		assert(response.status_code == STATUS_CODE[0])
		assert(response.json()['iso'] == 'SVK')
		assert(response.json()['match_count'] == 3)
		assert(self.compare_list(response.json()['matches'],
								 ['Slowakei', 'Slovaška', 'Szlovákia']))
		# Test request 2
		response = requests.post(BASE + "match_country", req_2)
		assert(response.status_code == STATUS_CODE[0])
		assert(response.json()['iso'] == 'ECU')
		assert(response.json()['match_count'] == 3)
		assert(self.compare_list(response.json()['matches'],
								 ['ඉක්වදෝරය', '에콰도르', 'Ekvádor']))
		# Test request 3
		response = requests.post(BASE + "match_country", req_3)
		assert(response.status_code == STATUS_CODE[0])
		assert(response.json()['iso'] == 'JPN')
		assert(response.json()['match_count'] == 0)
		assert(len(response.json()['matches']) == 0)

	def test_invalid_requests(self):
		# Test request 4
		response = requests.post(BASE + "match_country", req_4)
		assert(response.status_code == STATUS_CODE[1])
		assert(str(response.json()['message']) == MESSAGES[1])
		# Test request 5
		response = requests.post(BASE + "match_country", req_5)
		assert(response.status_code == STATUS_CODE[1])
		assert(str(response.json()['message']) == MESSAGES[2])
		# Test request 6
		response = requests.post(BASE + "match_country", req_6)
		assert(response.status_code == STATUS_CODE[1])
		assert(str(response.json()['message']) == MESSAGES[1])
		# Test request 6
		response = requests.post(BASE + "match_country", req_7)
		assert(response.status_code == STATUS_CODE[2])
		assert(response.json()['message'] == MESSAGES[0])
