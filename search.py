from googlesearch import search

"""
query : query string that we want to search for.
tld : tld stands for top level domain which means we want to search our result on google.com or google.in or some other domain.
lang : lang stands for language.
num : Number of results we want.
start : First result to retrieve.
stop : Last result to retrieve. Use None to keep searching forever.
pause : Lapse to wait between HTTP requests. Lapse too short may cause Google to block your IP. Keeping significant lapse will make your program slow but its safe and better option.
Return : Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop forever.
"""

class Stalk:
    tld = "co.in"
    num = 10
    stop = 10

    def __init__(self, email):
        self.email = email
    
    def write(self, data):
        """
        Write data to a file named with the users email
        """
        writable_data = {self.email: data}
        with open(f"{str(self.email)}.txt", "w") as email_file:
            email_file.write(str(writable_data))

    def search(self, query):
        """
        Search for results with a query and return a list of links returned by the search
        """
        self.results = []
        for result in search(query, tld=self.tld, num=self.num, stop=self.stop, pause=self.pause):
            self.results.append(result)

        return self.results
    