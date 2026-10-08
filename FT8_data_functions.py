"""Helpers for loading and filtering FT8 contest data from the project Excel sheet."""
# Author: Jeff Tubbenhauer VK5IU
# Date 07/10/2026

import pandas as pd

from pathlib import Path

DATA_FILE = Path("data/datasheet.xlsx")

def _load_datasheet(file_path: str | Path = DATA_FILE) -> pd.DataFrame:
    """Read the FT8 datasheet and normalize common string and numeric fields."""
    df = pd.read_excel(file_path, keep_default_na=False)

    for column in [
        "BAND",
        "YEAR",
        "A_INDEX",
        "K_INDEX",
        "SFI",
        "MONTH",
        "TIME_ADL",
        "DISTANCE",
        "CALL",
    ]:
        if column in df.columns:
            df[column] = df[column].astype(str).str.strip()

    numeric_columns = [
        "DISTANCE",
        "SFI",
        "A_INDEX",
        "K_INDEX",
        "RST_SENT",
        "RST_RCVD",
    ]
    for column in numeric_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")

    if "TIME_ADL" in df.columns:
        df["TIME_ADL"] = pd.to_datetime(df["TIME_ADL"], format="%H:%M:%S", errors="coerce").dt.time

    if "DATE" in df.columns:
        date_values = df["DATE"].astype(str).str.strip()
        year_first = date_values.str.match(r"^\d{4}[-/]\d{1,2}[-/]\d{1,2}")
        parsed_dates = pd.to_datetime(date_values.where(year_first), errors="coerce")
        day_first_dates = pd.to_datetime(
            date_values.where(~year_first),
            dayfirst=True,
            errors="coerce",
        )
        df["DATE"] = parsed_dates.fillna(day_first_dates)

    return df


def get_my_data(band_type, year_type):
    """Fetch and clean FT8 data for one band and one year."""
    df = _load_datasheet()

    band_value = str(band_type).strip()
    year_value = str(year_type).strip()

    mask = (df["BAND"] == band_value) & (df["YEAR"] == year_value)
    columns = [
        "BAND",
        "MONTH",
        "RST_RCVD",
        "RST_SENT",
        "A_INDEX",
        "K_INDEX",
        "SFI",
        "TIME_ADL",
        "DATE",
        "CALL",
        "DISTANCE",
    ]
    data = df.loc[mask, columns].copy()

    if data.empty:
        print("Your selection does not have band and/or year data!")
        return None

    data = data.sort_values(by="DATE", na_position="last").reset_index(drop=True)
    
    return data


def get_my_band_all_data(band_type):
    """Fetch all rows for the selected band across all years."""
    df = _load_datasheet()
    band_value = str(band_type).strip()
    mask = df["BAND"] == band_value

    columns = [
        "BAND",
        "MONTH",
        "RST_RCVD",
        "RST_SENT",
        "A_INDEX",
        "K_INDEX",
        "SFI",
        "TIME_ADL",
        "DATE",
        "YEAR",
    ]
    data = df.loc[mask, columns].copy()
    if data.empty:
        return data

    data = data.sort_values(by="DATE", na_position="last").reset_index(drop=True)
    return data


def get_data_for_year(year_type):# gdfy
    """Return all data rows for a specific year."""
    df = _load_datasheet()
    year_value = str(year_type).strip()
    mask = df["YEAR"] == year_value

    columns = [
        "DATE",
        "RST_RCVD",
        "RST_SENT",
        "MONTH",
        "CALL",
        "BAND",
        "YEAR",
        "A_INDEX",
        "K_INDEX",
        "SFI",
        "TIME_ADL",
        "DISTANCE",
    ]
    data = df.loc[mask, columns].copy()
    if data.empty:
        return data
    data['DATE'] = pd.to_datetime(data['DATE'], dayfirst=True, errors='coerce')
    data = data.sort_values(by="DATE", na_position="last").reset_index(drop=True)
    data['DATE'] = data['DATE'].dt.strftime('%d-%m-%Y')
    return data


def _first_available_band_year() -> tuple[str, str]:
    """Return a real band/year pair present in the Excel workbook."""
    df = _load_datasheet()
    if df.empty:
        return "20m", "2025"

    valid_pairs = df[["BAND", "YEAR"]].drop_duplicates().copy()
    valid_pairs["BAND"] = valid_pairs["BAND"].astype(str).str.strip()
    valid_pairs["YEAR"] = valid_pairs["YEAR"].astype(str).str.strip()

    if valid_pairs.empty:
        return "20m", "2025"

    first_row = valid_pairs.iloc[0]
    return str(first_row["BAND"]), str(first_row["YEAR"])

def get_all_data(my_data='data/datasheet.xlsx'):
    """Return all data rows, sorted by DATE as datetime values."""
    file_path = Path(my_data)
    if not file_path.is_absolute():
        file_path = Path(__file__).resolve().parent / file_path
    df = _load_datasheet(file_path)

    columns = [
        "DATE",
        "RST_RCVD",
        "RST_SENT",
        "MONTH",
        "CALL",
        "BAND",
        "YEAR",
        "A_INDEX",
        "K_INDEX",
        "SFI",
        "TIME_ADL",
        "DISTANCE",
    ]
    data = df.loc[:, columns].copy()
    data = data.dropna(subset=["DATE"]).sort_values("DATE").reset_index(drop=True)
    return data

if __name__ == "__main__":
    sample_band, sample_year = _first_available_band_year()
    sample_data = get_my_data(band_type=sample_band, year_type=sample_year)
    if sample_data is not None:
        print(f"Sample data for {sample_band} / {sample_year}:")
        print(sample_data.head())
    else:
        print(f"No data found for {sample_band} / {sample_year}.")

    band_data = get_my_band_all_data(band_type=sample_band)
    if not band_data.empty:
        print(f"Band data for {sample_band}:")
        print(band_data.head())

    year_data = get_data_for_year(year_type=sample_year)
    if not year_data.empty:
        print(f"Year data for {sample_year}:")
        print(year_data.head())

    def get_all_data(my_data='data/datasheet.xlsx'):
        if my_data is None:
            my_data = 'data/datasheet.xlsx'
       
       
        return get_all_data(my_data=my_data)
    
