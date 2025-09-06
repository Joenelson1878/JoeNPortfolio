import pandas as pd 

CATEGORY_KEYWORDS = {
    "Food": [
        "restaurant", "dinner", "lunch", "breakfast", "brunch", "meal",
        "groceries", "supermarket", "cafe", "coffee", "tea", "snacks",
        "takeaway", "fast food", "pizza", "burger", "sandwich", "drink",
        "beverage", "alcohol", "bar", "pub", "bakery", "butcher"
    ],
    
    "Transport": [
        "train", "uber", "taxi", "bus", "fuel", "petrol", "diesel",
        "subway", "metro", "tram", "ride", "flight", "plane", "airfare",
        "car", "parking", "toll", "lyft", "cab", "scooter", "bike",
        "bicycle", "ferry", "transportation"
    ],
    
    "Entertainment": [
        "netflix", "spotify", "cinema", "movie", "film", "games",
        "gaming", "concert", "music", "theatre", "show", "event",
        "tickets", "festival", "hulu", "disney", "prime video",
        "youtube", "amusement", "arcade", "sports", "match", "stadium"
    ],
    
    "Rent": [
        "rent", "landlord", "apartment", "flat", "house", "lease",
        "tenancy", "rental", "housing", "lodging", "room", "accommodation"
    ],
    
    "Utilities": [
        "electricity", "gas", "water", "internet", "wifi", "broadband",
        "heating", "cooling", "power", "energy", "utility bill",
        "sewage", "trash", "waste", "telephone", "mobile bill"
    ],
    
    "Income": [
        "salary", "bonus", "paycheck", "wage", "payment", "earnings",
        "commission", "stipend", "income", "payout", "transfer",
        "interest", "dividend", "freelance", "side hustle", "allowance"
    ]
}

