import mysql.connector
import pprint

# Setup connection

mydb = mysql.connector.connect(
     host='localhost',
     user='root',
     password='Raspberry',
     port='3306',
     database='airiowa'
)

mycursor = mydb.cursor()
dcursor = mydb.cursor(dictionary=True)

# mycursor.execute("SQL CODE")
# mydb.commit()
# mycursor.fetchall()

# dcursor.execute('SELECT * FROM user_information WHERE 
#                  user_email = %s AND userid = %s',(email, ID))
# account = dcursor.fetchone()

# Call all the stored procedures
# FETCH_PROCEDURES
results = []


dcursor.callproc("fetch_invoice",('Ben', 'Lange'))
for result in dcursor.stored_results():
    # print(result.fetchall())
    results.append(result.fetchall())
print("")  
print("FETCH_INVOICE RESULTS")
print("--------------------------------------------------")
# print(results)
pp = pprint.PrettyPrinter(depth=10)
pp.pprint(results)

results.clear()


# FETCH_PASSENGERS

dcursor.callproc("fetch_passengers",[3])
for result in dcursor.stored_results():
    # print(result.fetchall())
    results.append(result.fetchall())
print("")
print("FETCH_PASSENGERS RESULTS")
print("--------------------------------------------------")
# print(results)
pp = pprint.PrettyPrinter(depth=10)
pp.pprint(results)

results.clear()

# GET_FLIGHT_DETAILS_GIVEN_ARRIVAL_DEPARTURE_LOCATION

dcursor.callproc("get_flight_details_given_arrival_departure_location",("Chicago", "Des Moines"))
for result in dcursor.stored_results():
    results.append(result.fetchall())
print("")
print("GET_FLIGHT_DETAILS_GIVEN_ARRIVAL_DEPARTURE_LOCATION RESULTS")
print("--------------------------------------------------")
# print(results)
pp = pprint.PrettyPrinter(depth=10)
pp.pprint(results)

results.clear()

# SEAT_CLASS_OPTION_GIVEN_FLIGHT_NUMBER

dcursor.callproc("seat_class_options_given_flight_number",[431])
for result in dcursor.stored_results():
    results.append(result.fetchall())
print("")
print("SEAT_CLASS_OPTION_GIVEN_FLIGHT_NUMBER RESULTS")
print("--------------------------------------------------")
# print(results)
pp = pprint.PrettyPrinter(depth=10)
pp.pprint(results)

results.clear()


# VIEW_FLIGHT_GIVEN_FLIGHT_NUMBER

dcursor.callproc("view_flight_given_flightnumber",[431])
for result in dcursor.stored_results():
    results.append(result.fetchall())
print("")
print("VIEW_FLIGHT_GIVEN_FLIGHT_NUMBER RESULTS")
print("--------------------------------------------------")
# print(results)
pp = pprint.PrettyPrinter(depth=10)
pp.pprint(results)

results.clear()

# VIEW_FLIGHT_GIVEN_FLIGHT_DAY

dcursor.callproc("view_flight_given_day",["2022-12-12"])
for result in dcursor.stored_results():
    results.append(result.fetchall())
print("")
print("VIEW_FLIGHT_GIVEN_FLIGHT_DAY RESULTS")
print("--------------------------------------------------")
# print(results)
pp = pprint.PrettyPrinter(depth=10)
pp.pprint(results)

results.clear()