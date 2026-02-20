from pathlib import Path
import pandas as pd

OUT_CSV = Path("data/citibike_2014_combined.csv")
# Columns we’ll normalize everything into (kept in this order)
CANON_ORDER = [
    "started_at", "ended_at", "trip_duration_sec",
    "start_station_id", "start_station_name", "start_lat", "start_lng",
    "end_station_id", "end_station_name", "end_lat", "end_lng",
    "bike_id", "user_type", "birth_year", "gender",
    "source_file",
]

def open_combined_csv(path: Path) -> pd.DataFrame:
    """Reads the combined CSV back in with the canonical columns and parsed datetimes."""
    return pd.read_csv(
        path,
        usecols=CANON_ORDER,
        parse_dates=["started_at", "ended_at"],
        dtype={
            "start_station_id": "string",
            "end_station_id": "string",
            "bike_id": "string",
            "user_type": "string",
            "birth_year": "string",
            "gender": "string",
            "source_file": "string",
        },
    )

if __name__ == "__main__":
    print("opening combined csv file")
    df = open_combined_csv(OUT_CSV)
    print("Combined shape:", df.shape)
    print(df.columns.tolist())
    df["trip_duration_sec"] = pd.to_numeric(df["trip_duration_sec"])
    df = df.dropna(subset=['gender','birth_year'])
    df["gender"] = pd.to_numeric(df["gender"],errors="coerce")
    df["birth_year"] = pd.to_numeric(df["birth_year"],errors="coerce")
    

    print("Average gender (1 male, 2 female):",df["gender"].mean())
    print("Average age of rider:", 2014-df["birth_year"].mean())
    print("Average trip duration (seconds):", df["trip_duration_sec"].mean())

    btotal = 0
    bcount = 0
    youngest_year = 0  # largest year = youngest person
    oldest_year = 9999 # smallest year = oldest person

    for by in df["birth_year"]:
        btotal = btotal + (2014-by)
        bcount = bcount + 1
        if by > youngest_year:
            youngest_year = by
        if by < oldest_year and by >= 1900:
            oldest_year = by

    genders = [0, 0, 0]
    gcount = 0
    for g in df["gender"]:
        genders[g] = genders[g] + 1
        gcount = gcount + 1
    percentages = [gtotal/gcount for gtotal in genders]
    
    print(genders)
    print(percentages)
    
    print(btotal)
    print(bcount)
    baverage = btotal / bcount
    print("Average age is", baverage)
    print("Youngest: ", 2014-youngest_year)
    print("Oldest: ", 2014-oldest_year)