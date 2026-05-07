# FT8_settings.py
def get_settings(settings):
    
    settings = {
            "bands":["6m", "10m", "12m", "15m", "17m", "20m", "30m", "40m", "80m", "160m"],
            "years":[str(year) for year in range(2023, 2027)],
            "default_band": "20m",
            "default_year": "2024"    
        }
    return settings   
