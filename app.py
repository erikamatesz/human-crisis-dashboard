import streamlit as st
from utils.fetch_data import get_acled_data
from utils.process_data import clean_acled_data
from utils.visualize import show_event_map
from config import COUNTRIES
import geocoder

st.set_page_config(page_title="Humanitarian Crisis Dashboard", layout="wide")
st.title("🌍 Humanitarian Crisis Dashboard – Real-time ACLED data")

col_country, col_start, col_end, col_event_types, col_button = st.columns([2, 1, 1, 3, 1])

with col_country:
    selected_country = st.selectbox("Country:", COUNTRIES)

with col_start:
    start_date = st.date_input("Start date", value=None)

with col_end:
    end_date = st.date_input("End date", value=None)

event_type_options = [
    "Protests",
    "Violence against civilians",
    "Battles",
    "Riots",
    "Strategic developments",
    "Explosions/Remote violence"
]

with col_event_types:
    selected_event_types = st.multiselect(
        "Event types (leave empty for all):",
        options=event_type_options,
        default=[],
    )

with col_button:
    st.markdown("""<div style="margin-top: 28px; display: flex; gap: 0.5rem">""", unsafe_allow_html=True)
    fetch_clicked = st.button("Fetch Data", key="fetch_button")
    st.markdown("</div>", unsafe_allow_html=True)

# Estado e funções permanecem iguais...

if "last_params" not in st.session_state:
    st.session_state.last_params = {}
if "data" not in st.session_state:
    st.session_state.data = None
if "map_center" not in st.session_state:
    st.session_state.map_center = None
if "message" not in st.session_state:
    st.session_state.message = ""
if "has_fetched_once" not in st.session_state:
    st.session_state.has_fetched_once = False

def get_user_location():
    try:
        g = geocoder.ip("me")
        if g.ok:
            return g.latlng
    except Exception:
        pass
    # fallback Lagos
    return [6.5244, 3.3792]

current_params = {
    "country": selected_country,
    "start_date": str(start_date) if start_date else None,
    "end_date": str(end_date) if end_date else None,
    "event_types": tuple(selected_event_types)
}
params_changed = current_params != st.session_state.last_params

if fetch_clicked:
    with st.spinner("Fetching data..."):
        try:
            raw_data = get_acled_data(country=selected_country, limit=1000)
            filtered_data = clean_acled_data(
                df=raw_data,
                start_date=current_params["start_date"],
                end_date=current_params["end_date"],
                event_types=selected_event_types if selected_event_types else None
            )

            st.session_state.data = filtered_data
            st.session_state.last_params = current_params
            st.session_state.has_fetched_once = True

            if not filtered_data.empty:
                st.session_state.map_center = [
                    filtered_data["latitude"].mean(),
                    filtered_data["longitude"].mean()
                ]
                st.session_state.message = f"✅ Loaded {len(filtered_data)} events for {selected_country}. Zoom in on the map to explore the events in more detail."
            else:
                st.session_state.map_center = get_user_location()
                st.session_state.message = f"⚠️ No events found for {selected_country} with the selected filters."

        except Exception as e:
            st.error(f"❌ Failed to load data: {e}")

if st.session_state.data is not None:
    base_msg = st.session_state.message
    if st.session_state.has_fetched_once and params_changed:
        base_msg += " ⚠️ If you change any parameter, click 'Fetch Data' again to refresh the results."
    st.info(base_msg)

if st.session_state.data is not None:
    if st.checkbox("Show filtered data table to download .CSV with data."):
        st.dataframe(st.session_state.data)

map_center = st.session_state.map_center if st.session_state.map_center else get_user_location()
show_event_map(st.session_state.data, center=map_center)
