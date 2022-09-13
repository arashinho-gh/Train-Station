class Convert_CSV:

    def get_adj_list(self):

        with open('./_dataset/london.connections.csv') as input:

            attributes = input.readline().strip().replace('"', "").split(",")

            connections = input.readlines()

            dataBase = {}

        for connection in connections:

            connection = connection.strip().split(",")

            station1 = connection[0]
            station2 = connection[1]
            line = connection[2]
            time = connection[3]
            
            if station1 not in dataBase:

                dataBase[station1] = {}

            if station2 not in dataBase[station1]:

                dataBase[station1][station2] = []

            dataBase[station1][station2].append( {
                "time" : time,
                "line" : line
            })

        print(dataBase.get('49').get('255'))

            
    def get_lines(self):

        with open('./_dataset/london.lines.csv') as input:

            attributes = input.readline().strip()

            lines = input.readlines()
            
            lines_dataBase = {}

            for line in lines:

                line = line.strip().split(",")
                
                line_id = line[0]
                name = line[1]
                colour = line[2]
                stripe = line[3]

                lines_dataBase[line_id] = {
                    "name" : name,
                    "colour" : colour,
                    "stripe": stripe
                }

    def get_stations(self):

        with open('./_dataset/london.stations.csv') as input:

            attributes = input.readline().strip()

            stations = input.readlines()

            stations_dataBase = {}

            for station in stations:

                station = station.strip().split(",")

                station_id = station[0]
                latitude = station[1]
                longitude = station[2]
                name = station[3]
                display_name = station[4]
                zone = station[5]
                total_lines = station[6]
                rail = station[7]
                
                stations_dataBase[station_id] = {
                    
                    "latitude":latitude,
                    "longitude" : longitude,
                    "name": name,
                    "display_name" : display_name,
                    "zone": zone,
                    "total_lines": total_lines,
                    "rail": rail

                }

            print(stations_dataBase)




             
    




            

        

test = Convert_CSV()

test.get_adj_list()