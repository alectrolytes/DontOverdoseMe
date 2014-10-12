from temboo.Library.DailyMed import SearchByName
from temboo.Library.DailyMed import GetComponents
from temboo.Library.DailyMed import Query
from temboo.core.session import TembooSession
import json

# Create a session with your Temboo account details
session = TembooSession("alectrolytes", "myFirstApp", "0a6f17f3866842f0b49be00de8d2dcd8")

# Instantiate the Choreo
searchByNameChoreo = SearchByName(session)

# Get an InputSet object for the Choreo
searchByNameInputs = searchByNameChoreo.new_input_set()

# Set the Choreo inputs
print("Enter Drug Name")
drug = raw_input()
searchByNameInputs.set_OutputFormat("json")
searchByNameInputs.set_DrugName(drug)

# Execute the Choreo
searchByNameResults = searchByNameChoreo.execute_with_results(searchByNameInputs)

# # Print the Choreo outputs
# print("Response: " + searchByNameResults.get_Response())

# Establish the Drug ID
a = json.loads(searchByNameResults.get_Response())
drugID = a['DATA'][-1][0]

# Instantiate the Choreo
getComponentsChoreo = GetComponents(session)

# Get an InputSet object for the Choreo
getComponentsInputs = getComponentsChoreo.new_input_set()

# Set the Choreo inputs
getComponentsInputs.set_SetID(drugID)

# Execute the Choreo
getComponentsResults = getComponentsChoreo.execute_with_results(getComponentsInputs)

# # Print the Choreo outputs
# print("Response: " + getComponentsResults.get_Response())

# Instantiate the Choreo
queryChoreo = Query(session)

# Get an InputSet object for the Choreo
queryInputs = queryChoreo.new_input_set()

# Set the Choreo inputs
queryInputs.set_Components("DRUG INTERACTIONS SECTION")
queryInputs.set_SetID(drugID)

# Execute the Choreo
queryResults = queryChoreo.execute_with_results(queryInputs)

# Print the Choreo outputs
print("Response: " + queryResults.get_Response())
