## DGY Thesis - Data Manipulation Code

#########################
## CODE INITIALISATION ##
#########################

# Import necessary packages
import pandas as pd
import numpy as np

###############
## LOAD DATA ##
###############

# Load scraped data for each frame size
frame150df = pd.read_csv("Frame150Data.csv")
frame200df = pd.read_csv("Frame200Data.csv")
frame250df = pd.read_csv("Frame250Data.csv")
frame300df = pd.read_csv("Frame300Data.csv")
frame350df = pd.read_csv("Frame350Data.csv")
frame400df = pd.read_csv("Frame400Data.csv")
frame450df = pd.read_csv("Frame450Data.csv")
frame500df = pd.read_csv("Frame500Data.csv")
frame550df = pd.read_csv("Frame550Data.csv")

print(frame150df)

# Convert all hyphen values to NaN 
frame150df = frame150df.replace('-',np.nan)
frame200df = frame200df.replace('-',np.nan)
frame250df = frame250df.replace('-',np.nan)
frame300df = frame300df.replace('-',np.nan)
frame350df = frame350df.replace('-',np.nan)
frame400df = frame400df.replace('-',np.nan)
frame450df = frame450df.replace('-',np.nan)
frame500df = frame500df.replace('-',np.nan)
frame550df = frame550df.replace('-',np.nan)


# Drop all NaN values from the dataframe
frame150dfClean = frame150df.dropna()
frame200dfClean = frame200df.dropna()
frame250dfClean = frame250df.dropna()
frame300dfClean = frame300df.dropna()
frame350dfClean = frame350df.dropna()
frame400dfClean = frame400df.dropna()
frame450dfClean = frame450df.dropna()
frame500dfClean = frame500df.dropna()
frame550dfClean = frame550df.dropna()


# Create a vector of all dataframes to concatenate
combinedDataFrames = [frame150dfClean,frame200dfClean,frame250dfClean,frame300dfClean,frame350dfClean,frame400dfClean,frame450dfClean,frame500dfClean,frame550dfClean]

dfComb = pd.concat(combinedDataFrames)

colNames = ['Weight','Frame','KV','NLC','NLV','LimCurrent','InternalR','motDiam','propDiam','propPitch','Blades','ESCCurrent','ESCCells','BattCells','BattCap','BattDischarge','Endurance','RemLoad','Range','MaxSpeed']

dfComb.columns = colNames

print(dfComb)

dfComb['RemLoad'] = dfComb['RemLoad'].astype(float)
dfComb['Endurance'] = dfComb['Endurance'].astype(float)
dfComb['Range'] = dfComb['Range'].astype(float)
dfComb['MaxSpeed'] = dfComb['MaxSpeed'].astype(float)

dfComb['MTOW'] = dfComb['Weight'] + dfComb['RemLoad']

print(dfComb)

dfComb.to_csv("combinedData.csv", index = False)