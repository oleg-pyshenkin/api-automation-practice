import requests
from config import BASE_URL

class PostClient:
    def __init__(self):
        self.url = f"{BASE_URL}/posts"

    def get_one(self, post_id):
        return requests.get(f"{self.url}/{post_id}")
    
    def create(self, payload):
        return requests.post(self.url, json=payload)
    
    def get_all(self):
        return requests.get(self.url)
    
    def delete(self, post_id):
        return requests.delete(f"{self.url}/{post_id}")

    def update (self, post_id, payload):
        return requests.put(f"{self.url}/{post_id}", json=payload)