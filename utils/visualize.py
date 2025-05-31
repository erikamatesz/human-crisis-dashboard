import streamlit as st
import pydeck as pdk
import pandas as pd

def show_event_map(df, center=None):
    if df is None or df.empty:
        st.pydeck_chart(pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state=pdk.ViewState(
                latitude=center[0] if center else 0,
                longitude=center[1] if center else 0,
                zoom=4,
                pitch=0,
            ),
            layers=[],
        ))
        return

    color_dict = {
        "Protests": [0, 0, 255],
        "Violence against civilians": [255, 0, 0],
        "Battles": [0, 255, 0],
        "Riots": [255, 165, 0],
        "Strategic developments": [128, 0, 128],
        "Explosions/Remote violence": [139, 0, 0],
    }

    def get_color(event_type):
        return color_dict.get(event_type, [128, 128, 128])

    df["color"] = df["event_type"].apply(get_color)

    df["event_date"] = pd.to_datetime(df["event_date"], errors="coerce")
    df["event_date"] = df["event_date"].dt.strftime("%d-%b-%Y")

    layer = pdk.Layer(
        "ScatterplotLayer",
        data=df,
        get_position="[longitude, latitude]",
        get_fill_color="color",
        get_radius=1500,
        pickable=True,
        auto_highlight=True,
    )

    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state=pdk.ViewState(
            latitude=df["latitude"].mean(),
            longitude=df["longitude"].mean(),
            zoom=4,
            pitch=0,
        ),
        layers=[layer],
        tooltip={
            "html": """
                <b>Type:</b> {event_type}<br/>
                <b>Sub-type:</b> {sub_event_type}<br/>
                <b>Actor 1:</b> {actor1}<br/>
                <b>Actor 2:</b> {actor2}<br/>
                <b>Date:</b> {event_date}<br/>
                <b>Fatalities:</b> {fatalities}
            """,
            "style": {"color": "white"},
        },
    ))
