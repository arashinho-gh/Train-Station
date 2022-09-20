class Metrics_Extractor:

    metrics = ()

    def __init__(self, file):

        with open(file, mode='r') as input:

            attributes = input.readline().strip().replace('"', "").split(",")

            data = input.readlines()

            res_data = []

            for d in data:

                d = d.strip().split(",")

                res_data.append(d)

        self.metrics = (attributes, res_data)


