import pyodbc
from data import server_info
from objects.map_data import MapData
from stats.map_winrate import TotalRates, SpecificRates

map_database = []

map_winrate_statistics = []

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server_info.SERVER + ';DATABASE=' + server_info.DATABASE + ';Trusted_Connection=' + server_info.TRUSTED)
cursor = conn.cursor()

cursor.execute("SELECT * FROM Maps")

results = cursor.fetchall()

for map_info in results:
    newObj = MapData(map_info[0], map_info[1], map_info[2], map_info[3], map_info[4], map_info[5], map_info[6], map_info[7], map_info[8])

    map_database.append(newObj)

conn.close()

print(TotalRates.get_total_map_rates(map_database))