import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def deck_sort(df):
    df.loc[df['deck'].isin(['A', 'B', 'C']), 'home planet'] = 'Europa'
    return df

def data_viz(df):
    """
    This function prepares the data very briefly for understanding and prepared some viasualizations.
    - cast columns CryoSleep and VIP as boolean values.
    - create dict to fill missing values.
    - dropping unnecessary columns (Cabin, name and number).
    - 
    """
    df[['Deck', 'Num', 'Side']] = df['Cabin'].str.split('/', expand=True)
    df[['Group', 'Number']] = df['PassengerId'].str.split('_', expand=True)
    
    df['TotalExpenses'] = df[['RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']].sum(axis=1)

    df["Destination"].fillna("Undisclosed", inplace=True) 
    df["HomePlanet"].fillna("Undisclosed", inplace=True)
    df["Deck"].fillna("Undisclosed", inplace=True) 
    df["Side"].fillna("Undisclosed", inplace=True) 

    df.drop(columns=["Cabin", "Name","Number"], inplace=True)

    df['CryoSleep'] = df['CryoSleep'].astype(bool)
    df['VIP'] = df['VIP'].astype(bool)

    df.sort_values(by='HomePlanet', inplace=True)
    df.sort_values(by='Deck', inplace=True)
    
    return df

def train_transform(df):
    """
    This function prepares the data for the model and fill some missing information according to the EDA's findings
    """
    # According to the findings, proper assign people to Decks
    df.loc[df['Deck'].isin(['A', 'B', 'C', 'T']), 'HomePlanet'] = 'Europa'
    df.loc[df['Deck'].isin(['G']), 'HomePlanet'] = 'Earth'

    # Crating a dictionary for the remaing data
    destination_dict = {"TRAPPIST-1e":1, "PSO J318.5-22":2,"55 Cancri e":3, "Undisclosed":4}
    df["Destination"].replace(destination_dict, inplace = True)

    home_dict = {"Europa":1, "Earth":2,"Mars":3, "Undisclosed":4}
    df["HomePlanet"].replace(home_dict, inplace = True)

    deck_dict = {"A":1, "B":2,"C":3, "D":4, "E":5, "F":6, "G":7, "T":8, "Undisclosed":9}
    df["Deck"].replace(deck_dict, inplace = True)

    side_dict = {"P":1, "S":2, "Undisclosed":3}
    df["Side"].replace(side_dict, inplace = True)

    #Standardizing large scales
    min_max_scaler = MinMaxScaler()
    df["Expenses_modified"] = min_max_scaler.fit_transform(df["TotalExpenses"].values.reshape(-1, 1))
    
    # dropping unecessary columns
    df.drop(columns=["RoomService", "FoodCourt", "ShoppingMall", "Spa", "VRDeck","TotalExpenses"], inplace = True)

    #correcting type casts
    df['Num'] = df['Num'].astype(float)
    df['Group'] = df['Group'].astype(int)
    df['Age'] = df['Age'].astype(float)

    return df