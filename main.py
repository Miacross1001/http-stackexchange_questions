import requests
from datetime import datetime

class SO_API:

    base_host = 'https://api.stackexchange.com/'

    def _get_unix_date(self):
        data_now = datetime.now()
        toDate = data_now.timestamp()

        to_date, to_time = str(data_now).split()
        to_date = to_date.split('-')
        to_date[0], to_date[1], to_date[2] = int(to_date[0]), int(to_date[1]), int(to_date[2]) - 2
        fromDate = datetime(to_date[0], to_date[1], to_date[2], 0, 0).timestamp()

        return fromDate, toDate

    def _get_quests(self):
        uri = "questions"
        params = {
            'site': 'ru.stackoverflow',
            'pagesize': 100
        }

        request_url = self.base_host + uri
        response = requests.get(request_url, params=params)
        return response.json()

    def search_quests(self):
        dict_quests = self._get_quests()
        fromDate, toDate = self._get_unix_date()
        result = []

        for item in dict_quests['items']:
            if 'python' in item['tags'] and fromDate <= item['creation_date'] <= toDate:
                title, link = item['title'], item['link']
                result.append([f'{title} - {link}'])

        return result


if __name__ == "__main__":
    api = SO_API()
    print(len(api.search_quests()))
    print(*api.search_quests(), sep='\n')
