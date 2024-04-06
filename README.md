# City-Data

Small tool for exploring data relevant to metro areas and cities in the US using a variety of sources.

## Setup

### General

Run

```bash
pip install -r requirements.txt
```

to install the dependencies.

### Census Data API Key

In order to use the US Census data API (required for accessing data from the American Community Survey, a.k.a. ACS), you should first create your own API key by navigating to and following instructions from the [census.gov api page](https://api.census.gov/data/key_signup.html).

Then, you should create a `.env.local` file and paste it in as the value for key `CENSUS_API_KEY`. In other words, you should add this entry to your `.env.local` file:

```.env
CENSUS_API_KEY=YOUR_API_KEY
```

where you replace `YOUR_API_KEY` with your actual API Key.
