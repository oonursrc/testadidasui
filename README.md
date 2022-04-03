
# jsonplaceholder

This project includes tests of Adidas UI.

Python with Selenium and BBD approach is used to develop UI tests.


## Run Locally

Install Python3 to your local machine

```bash
  https://www.python.org/downloads/
```

Clone the project

```bash
  https://github.com/oonursrc/testadidasui.git
```

Go to the project directory

```bash
  cd testadidasui
```

Create python virtual env

```bash
  python3 -m venv venv
```

Activate virtual env

```bash
  . venv/bin/activate
```

Install required packages

```bash
  pip install -r requirements.txt
```


## Running Tests

To run tests, run the following command

```bash
  python3 -m pytest tests/step_defs/steps.py --junitxml=test-reports/report.xml
```


## CircleCI

To run tests on CircleCI, run the following link

[CircleCI Page](https://app.circleci.com/pipelines/github/oonursrc/testadidasui?branch=main)
## FAQ

If you have Python SSL issue, please follow the link below

[Link](https://github.com/actions/setup-python/issues/93/)
