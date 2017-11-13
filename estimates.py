import pandas as pd
import numpy as np
import re

def clean_neighbourhood(text):
    text = re.sub(r"/|\s|-|'", "", text.lower())
    if text == "civiccenter" or text == "tenderloin" or text == "unionsquare":
        return "downtown"
    elif text == "westernadditionnopa" or text == "alamosquare" or text == "fillmoredistrict" or text == "hayesvalley" or text == "japantown" or text == "lowerhaight":
        return "westernaddition"
    elif text == "dogpatch":
        return "potrerohill"
    elif text == "balboaterrace" or text == "foresthill" or text == "westportal":
        return "westoftwinpeaks"
    elif text == "colevalley":
        return "haightashbury"
    elif text == "cowhollow":
        return "marina"
    elif text == "dubocetriangle":
        return "thecastro"
    elif text == "fishermanswharf" or text == "telegraphhill":
        return "northbeach"
    elif text == "ingleside":
        return "oceanview"
    elif text == "missionbay":
        return "soma"
    elif text == "sunnyside":
        return "outermission"
    elif text == "portola":
        return "excelsior"
    elif text == "southbeach":
        return "financialdistrict"
    else:
        return text

def get_neighborhood(lat, lon):
	lat = float(lat)
	lon = float(lon)
	listings = pd.read_csv("listings.csv") 
	lat_lon = listings[["latitude", "longitude", "neighbourhood"]].dropna()
	print(lat_lon[:1])
	distances = np.sqrt((lat_lon["latitude"] - lat) ** 2 + (lat_lon["longitude"] - lon) ** 2)
	min_idx = np.argmin(distances)
	lat_lon["neighbourhood"] = lat_lon["neighbourhood"].apply(clean_neighbourhood)
	return lat_lon.loc[min_idx, "neighbourhood"]

def estimate_weekly_rev(lat, lon):
	neighbourhood = get_neighborhood(lat, lon)
	results = pd.read_csv("avg_weekly_revenue_neighbourhood.csv")
	return results[results["neighbourhood"] == neighbourhood].iloc[0,3]

def estimate_ideal_price(lat, lon):
	neighbourhood = get_neighborhood(lat, lon)
	results = pd.read_csv("max_rev.csv")
	return results[results["neighbourhood"] == neighbourhood].iloc[0,3] 

