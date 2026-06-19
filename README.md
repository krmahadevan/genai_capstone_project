# Fake News Room

This is a sample capstone project that was aimed at re-inforcing whatever I learnt.

## Pre-requisite

* Create a GEMINI Key from [here](https://aistudio.google.com/api-keys)
* Create a `.env` file which includes the Gemini key. Here's a sample of how the file can look like:

```dotenv
GEMINI_API_KEY=BlahBlahKeyContentsGoesHere

```

## Developer setup

* Initialize the virtual environment using:

```bash
python3 -m venv .venv
```

* Activate the virtual environment using:

```bash
source .venv/bin/activate
```

* Install the dependencies using:

```bash
pip3 install -r requirements.txt
```

* Run the sample application using:

```bash
streamlit run news_generator.py
```