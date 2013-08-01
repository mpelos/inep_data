class EnemParser(object):
    def parse(self, string):
        data = {}
        data["school_id"] = self._get_data(string, 203, 8)
        data["city_id"] = self._get_data(string, 213, 4)
        data["state_id"] = self._get_data(string, 211, 2)
        data["city"] = self._get_data(string, 218, 150)
        data["state"] = self._get_data(string, 368, 2)

        scores = data["scores"] = {}
        scores["nature_science"] = self._get_data(string, 536, 9)
        scores["human_science"] = self._get_data(string, 545, 9)
        scores["languages"] = self._get_data(string, 554, 9)
        scores["mathematics"] = self._get_data(string, 563, 9)

        return data

    def _get_data(self, string, position, length):
        data = string[position:position + length].strip()
        data = data.replace("\n", "")

        if data == ".": data = ""

        try:
            data = int(float(data))
        except ValueError:
            pass

        return data
