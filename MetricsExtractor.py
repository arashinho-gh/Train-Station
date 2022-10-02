class Metrics_Extractor:

    metrics = ()

    def __init__(self, file):

        with open(file, mode='r') as input:

            attributes = input.readline().strip().replace('"', "").split(",")

            data = input.readlines()

            res_data = []

            for d in data:
                
                temp = ""

                if ", " in d:
            
                    d = d.strip().replace(", ", "#").split(",")
                    temp = d

                else:

                    d = d.strip().split(",")
                    temp = d

                for i in range(len(d)):
                    if "#" in d[i]:
                        d[i] = d[i].replace("#", ", ")

                res_data.append(temp)

        self.metrics = (attributes, res_data)


