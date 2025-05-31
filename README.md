# 🌍 Humanitarian Crisis Dashboard

This Streamlit application visualizes real-time data on humanitarian crises around the world, using the ACLED (Armed Conflict Location & Event Data) API. Users can filter data by country, date range, and event types, and view them on an interactive map.

## 🔎 Features

- Real-time data fetching from the [ACLED API](https://acleddata.com/)
- Filter by:
  - Country
  - Start and end date
  - Event types (e.g., Protests, Riots, Violence against civilians, etc.)
- Interactive map with color-coded events
- Option to view and download filtered data as CSV

## 📦 Technologies Used

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Requests](https://docs.python-requests.org/)
- [PyDeck](https://deckgl.readthedocs.io/en/latest/)
- [Geocoder](https://geocoder.readthedocs.io/)

## 🚀 How to Run Locally (macOS / Linux)

1. Clone the repository:

```bash
git clone https://github.com/erikamatesz/crisis_dashboard.git
cd crisis_dashboard
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

## 📌 Notes
- Data is retrieved via ACLED API with a limit of 1000 events per request.
- Coordinates and event dates are cleaned before visualization.
- Events are color-coded for clarity.

--

☸️ May all sentient beings be free from suffering. 