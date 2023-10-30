## DGY Thesis - flyeval Data Extraction Script

#########################
## CODE INITIALISATION ##
#########################

# Import Packages
import selenium
import webdriver_manager
import time
import pandas as pd
import numpy as np

# Import Subpackages from previously installed packages
from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch Firefox Driver
driver = webdriver.Firefox()

# Define access url
url = "http://flyeval.com"

########################
## DATAFRAME CREATION ##
########################

# Create an empty dataframe using Pandas
df = pd.DataFrame()

###########################
## VARIABLE INTRODUCTION ##
###########################

# This section introduces the variables that are discrete and are not affected by previous parameters such as frame size

# Altitude
alt = 0

# Ambient Temperature
tempC = 15

# Battery Cells
battCells = [2,3,4]

# Blade Numbers
bladeNos = 2

# No Load Current
noLoadCurrent = 0.1

# No Load Voltage
noLoadVoltage = 10

# Internal Resistance
internalR = 50

# Limit Current
limCurr = 10

#####################################
## WEBPAGE VARIABLE IDENTIFICATION ##
#####################################

# These variables refer to the IDs used in the Webpage

# Total WEight
evalWeight = "inTWeight"

# Frame Size
evalFrame = "inFrLen"

# Altitude
evalAlt = "inAlt"

# Ambient Temperature
evalTemp = "inTemp"

# Motor KV
evalKV = "inMotorKv"

# No Load Current
evalNLC = "inNoLoCur"

# No Load Voltage
evalNLV = "inNoLoVo"

# Limit Current
evalLimCurrent = "inMotorLimitCur"

# Internal Resistance
evalInternalR = "inMotorR"

# Motor Diameter
evalMotorDiam = "inChoOutLen"

# Propeller Diameter
evalPropDiam = "inPropDia"

# Propeller Pitch
evalPropPitch = "inPropPitch"

# ESC Discharge Current
evalESCCurrent = "inESCContI"

# Number of Battery Cells
evalBattCells = "inBattSeries"

# Battery Capacity
evalBattCap = "inBattCapa"

# Max Batt Current
evalBattCurr = "inBattCur"

# Motor Brand - CUSTOMISED
evalMotor = "inMotorBrand_chzn_o_0"

# ESC Brand - CUSTOMISED
evalESC = "inESCBrand_chzn_o_0"

# Prop Brand - CUSTOMISED
evalProp = "inPropBrand_chzn_o_0"

# Battery Brand - CUSTOMISED
evalBatt = "inBattBrand_chzn_o_0"

# Limit Current
evalLimCurr = "inMotorLimitCurType"
evalLimCurrVal = 1

# Prop Blades
evalBladeNo = "inPropblade"
evalBladeNoVal = 2

# ESC Cells
evalESCCells = "inESCMaxV"
evalESCCellsVal = 4

# Battery Type
evalBattType = "inBattType1"
evalBattTypeVal = 0

# Number of Blades
evalNumBlades = "inPropBlade"

#####################
## STRING CREATION ##
#####################

# Script requires JS queries executed in the Python environment - create query strings

# Default element by ID query string
queryStr1 = "document.getElementById('"
queryStr2 = "')"

# Value Query String
valueQueryStr1 = ".value='"
valueQueryStr2 = "'"

# Element Clicking String
clickStr  = ".click()"


###############################
## FRAME-SPECIFIC PARAMETERS ##
###############################

# Weights
totWeight = [1,0.9,0.8,0.7,0.6]

# Frame Size
frameSize = 250

# Propeller Diameter
propDiam = 5

# Motor KVs
motKV = [3000,2750,2500,2250,2000]

# Motor Diameters
motDiam = [18,16,14]

# Prop Pitch
propPitch = [7,6,5,4]

# ESC Discharge Current
escCurrent = [10,20]

# Battery Capacity
battCap = [2000,1750,1500,1250,1000]

# Battery Discharge
battDisc = [10, 20]

###################################
## VARIABLE ITERATION & SCRAPING ##
###################################

# This section will identify the variables to be iterated through, as well as setting constant variables
# The scraping and data storage process will be completed in this section as well

## 1. LAUNCH WEBPAGE
driver.get(url)

## 2. SET FIXED FIELDS

# Set Motor Brand to Customised
motorStr = queryStr1+evalMotor+queryStr2+clickStr
driver.execute_script(motorStr)
time.sleep(0.75)
driver.execute_script(motorStr)

# Set Prop Brand to Customised
propStr = queryStr1+evalProp+queryStr2+clickStr
driver.execute_script(propStr)
time.sleep(0.75)
driver.execute_script(propStr)

# Set ESC Brand to Customised
ESCstr = queryStr1+evalESC+queryStr2+clickStr
driver.execute_script(ESCstr)
time.sleep(0.75)
driver.execute_script(ESCstr)

# Set Battery Brand to Customised
battStr = queryStr1+evalBatt+queryStr2+clickStr
driver.execute_script(battStr)
time.sleep(0.75)
driver.execute_script(battStr)

# Set Limit Current Units to Amps (Will not change)
limCurrStr = queryStr1+evalLimCurr+queryStr2+valueQueryStr1+str(evalLimCurrVal)+valueQueryStr2
print(limCurrStr)
driver.execute_script(limCurrStr)

time.sleep(0.25)

# Set maximum ESC LiPo Support to 5 cells (Max. Investigated)
ESCCellStr = queryStr1+evalESCCells+queryStr2+valueQueryStr1+str(evalESCCellsVal)+valueQueryStr2
driver.execute_script(ESCCellStr)

time.sleep(0.25)

# Set Frame Size
frameSizeStr = queryStr1+evalFrame+queryStr2+valueQueryStr1+str(frameSize)+valueQueryStr2
driver.execute_script(frameSizeStr)

time.sleep(0.25)

# Altitude
altStr = queryStr1+evalAlt+queryStr2+valueQueryStr1+str(alt)+valueQueryStr2
driver.execute_script(altStr)

time.sleep(0.25)

# Set Temperature to 15 degrees C
tempStr = queryStr1+evalTemp+queryStr2+valueQueryStr1+str(tempC)+valueQueryStr2
driver.execute_script(tempStr)

time.sleep(0.25)

# Set No Load Current
NLCstr = queryStr1+evalNLC+queryStr2+valueQueryStr1+str(noLoadCurrent)+valueQueryStr2
driver.execute_script(NLCstr)

time.sleep(0.25)

# Set No Load Voltage
NLVstr = queryStr1+evalNLV+queryStr2+valueQueryStr1+str(noLoadVoltage)+valueQueryStr2
driver.execute_script(NLVstr)

time.sleep(0.25)

# Set Limit Current
limCurrValStr = queryStr1+evalLimCurrent+queryStr2+valueQueryStr1+str(limCurr)+valueQueryStr2
driver.execute_script(limCurrValStr)

time.sleep(0.25)

# Set Internal Resistance
intRStr = queryStr1+evalInternalR+queryStr2+valueQueryStr1+str(internalR)+valueQueryStr2
driver.execute_script(intRStr)

time.sleep(0.25)

# Set Prop Diameter
propDiamStr = queryStr1+evalPropDiam+queryStr2+valueQueryStr1+str(propDiam)+valueQueryStr2
driver.execute_script(propDiamStr)

time.sleep(0.25)

# Set Blade Numbers
bladeNoStr = queryStr1+evalBladeNo+queryStr2+valueQueryStr1+str(bladeNos)+valueQueryStr2
driver.execute_script(bladeNoStr)

time.sleep(0.25)

#######################
## ITERATIVE LOOPING ##
#######################


# Battery Discharge
for discharges in battDisc:
    
    # Discharge Query
    battDischargeQuery = queryStr1+evalBattCurr+queryStr2+valueQueryStr1+str(discharges)+valueQueryStr2
    driver.execute_script(battDischargeQuery)
    
    # Number of Battery Cells
    for cells in battCells:
        
        # Battery Cell Query
        battCellQuery = queryStr1+evalBattCells+queryStr2+valueQueryStr1+str(cells)+valueQueryStr2
        driver.execute_script(battCellQuery)
        
        # ESC Discharge Currents
        for currents in escCurrent:
            
            # ESC Discharge Current Query
            ESCDischargeQuery = queryStr1+evalESCCurrent+queryStr2+valueQueryStr1+str(currents)+valueQueryStr2
            driver.execute_script(ESCDischargeQuery)
            
            # Battery Capacities
            for caps in battCap:
                
                # Battery Capacity Query
                battCapQuery = queryStr1+evalBattCap+queryStr2+valueQueryStr1+str(caps)+valueQueryStr2
                driver.execute_script(battCapQuery)
                
                
                # Propeller Pitches
                for pitches in propPitch:
                    
                    # Propeller Pitch Query
                    pitchQuery = queryStr1+evalPropPitch+queryStr2+valueQueryStr1+str(pitches)+valueQueryStr2
                    driver.execute_script(pitchQuery)
                    
                    # Motor Diameters
                    for diameters in motDiam:
                        
                        # Motor Diameter Query
                        motDiamQuery = queryStr1+evalMotorDiam+queryStr2+valueQueryStr1+str(diameters)+valueQueryStr2
                        driver.execute_script(motDiamQuery)
                        
                        # Motor KVs
                        for kvs in motKV:
                            
                            # KV Query
                            kvQuery = queryStr1+evalKV+queryStr2+valueQueryStr1+str(kvs)+valueQueryStr2
                            driver.execute_script(kvQuery)
                            
                            # Weights
                            for weights in totWeight:
                            
                                # Form Weight Query
                                weightQuery = queryStr1+evalWeight+queryStr2+valueQueryStr1+str(weights)+valueQueryStr2
                                driver.execute_script(weightQuery)
                                
                                time.sleep(0.5)
                                
                                # Click calculation button
                                driver.execute_script("document.getElementById('inCalcButton').click()")
                                
                                time.sleep(1.5)
                                
                                # Specify variables for range, endurance, top speed and remaining weight
                                ranges = driver.find_elements(By.ID, "outFlyRange")
                                maxSpeeds  = driver.find_elements(By.ID,"outForSpeed")
                                endurances = driver.find_elements(By.ID,"outHoverTime")
                                remLoads = driver.find_elements(By.ID,"outLoadWeight")
                                
                                # Iterate through each output variable and extract the value
                                for ri in ranges:
                                    flyRange = ri.text
                                
                                
                                for mi in maxSpeeds:
                                    maxSpeed = mi.text
                                

                                for ei in endurances:
                                    endurance = ei.text
                                
                                
                                for li in remLoads:
                                    remLoad = li.text
                                    
                                    
                                    
                                # Formulate the vector of inputs and results
                                resultsVec = [weights, frameSize, kvs, noLoadCurrent, noLoadVoltage, limCurr, internalR, diameters, propDiam, pitches, bladeNos, currents, evalESCCellsVal, cells, caps, discharges, endurance,remLoad,flyRange,maxSpeed]
                                
                                # Print results vector for debug purposes
                                print(resultsVec)
                                
                                # Write results into a dataframe
                                df = pd.concat([df, pd.DataFrame([resultsVec])], ignore_index=True)
                                
                                
# Export DataFrame to CSV
df.to_csv("Frame250Data.csv", index = False)