# Match_Country
Match_Country is a microservice, that is able to take a country ISO code and a list of country names (in different languages) as an input. It will filter out just the countries that correspond to the provided ISO code and return them as response in JSON format.

Below, and example of a request/response can be found:

Request:

```
POST /match_country

{
	"iso": "svk",
	"countries": [
		"iran",
		"Slowakei",
		"Vatikan",
		"Slovaška",
		"Szlovákia",
		"Belgrade",
		"España",
		"Nizozemsko"
	]
}
```

Response:
```
{
	"iso": "svk",
	"match_count": 3,
	"matches": [
		"Slowakei",
		"Slovaška",
		"Szlovákia"
	]
}
```

## Environment
Use the package manager [pip](https://pip.pypa.io/en/stable/) or [conda](https://docs.conda.io/en/latest/) to needed libraries:
```bash
$ pip install -r _env_requirements/requirements_pip.txt
# or
$ conda create --name <env> --file _env_requirements/requirements_conda.txt
```

## Usage
Two consoles are needed to simulate a REST API application. After activating the environment, run in one console the main.py script:

```bash
(myenv)
$ python src/main.py
 * Serving Flask app 'main' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 211-202-527
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```
And on the other you can submit POST requests. A test script has been created and you can run it using 'pytest'

```bash
(myenv)
$ pytest
============================================== test session starts ===============================================
platform win32 -- Python 3.10.0, pytest-7.1.1, pluggy-1.0.0
collected 2 items

test\test_match_country.py ..                                                                               [100%]

=============================================== 2 passed in 5.96s ================================================

```

Also, a jupiter notebook file has been created to test the code interactively.
