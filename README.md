# 🌍 Humanitarian Crisis Dashboard

This Streamlit application visualizes real-time data on humanitarian crises around the world, using the ACLED (Armed Conflict Location & Event Data) API. Users can filter data by country, date range, and event types, and view them on an interactive map.

🔗 **Live App**: [https://humanitarian-crisis-dashboard.streamlit.app/](https://humanitarian-crisis-dashboard.streamlit.app/)

## 🔎 Features

- Real-time data fetching from the [ACLED API](https://acleddata.com/)
- Filter by:
  - Country
  - Start and end date
  - Event types (e.g., Protests, Riots, Violence against civilians, etc.)
- Interactive map with color-coded events (zoom in to explore regions)
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
git clone https://github.com/erikamatesz/human-crisis-dashboard.git
cd human-crisis-dashboard
```

2. (Optional but recommended) Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
streamlit run app.py
```

## 📌 Notes
- Data is retrieved via ACLED API with a limit of 1000 events per request.
- Coordinates and event dates are cleaned before visualization.
- Events are color-coded for clarity.
- Zoom into the map to explore events more precisely.

## 🦄 About the Author
Developed by me, **Erika Matesz Bueno**, Data Scientist. 

Feel free to reproduce and, most importantly, teach others how to do it.

If you want to create a free training to teach others or have any questions, feel free to [contact me](https://www.linkedin.com/in/mateszbueno/).


---

☸️ May all sentient beings be free from suffering. 