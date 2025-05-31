import pandas as pd

def clean_acled_data(
    df: pd.DataFrame,
    start_date: str = None,
    end_date: str = None,
    event_types: list[str] = None
) -> pd.DataFrame:

    if df is None or df.empty:
        columns = ["latitude", "longitude", "event_date", "event_type"]
        return pd.DataFrame(columns=columns)

    df["latitude"] = pd.to_numeric(df.get("latitude"), errors="coerce")
    df["longitude"] = pd.to_numeric(df.get("longitude"), errors="coerce")

    # drop rows with missing coordinates
    df = df.dropna(subset=["latitude", "longitude"])

    # convert event_date to datetime coercing errors to NaT
    df["event_date"] = pd.to_datetime(df.get("event_date"), errors="coerce")

    # filter by start_date if provided
    if start_date:
        start_dt = pd.to_datetime(start_date)
        df = df[df["event_date"] >= start_dt]

    # filter by end_date if provided
    if end_date:
        end_dt = pd.to_datetime(end_date)
        df = df[df["event_date"] <= end_dt]

    # filter by event types if provided
    if event_types:
        df = df[df["event_type"].isin(event_types)]

    return df
