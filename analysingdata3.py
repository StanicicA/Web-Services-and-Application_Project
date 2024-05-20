from webbrowser import get
from analysingdata2 import getAll

data = getAll()
totalArea = 0
for entry in data:
    valuationReports = entry["ValuationReport"]
    for valuationReport in valuationReports:
        
        #if valuationReport["FloorUse"] == "HAIR SALON":
            #print (valuationReport["Area"],"+", totalArea,"=", end="")
        totalArea += valuationReport["Area"]
            #print(totalArea)

print (totalArea)