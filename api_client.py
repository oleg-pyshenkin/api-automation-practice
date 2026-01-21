import requests
import allure
import json

class PostClient:
    def __init__(self, base_url):
        self.url = f"{base_url}/posts"

    def _attach_details(self, response):
        allure.attach(
            f"Method: {response.request.method}\nURL: {response.url}",
            name="Request Info",
            attachment_type=allure.attachment_type.TEXT
        )
        allure.attach(
            json.dumps(response.json(), indent=4),
            name="Response Body",
            attachment_type=allure.attachment_type.JSON
        )


    def get_one(self, post_id):
        response = requests.get(f"{self.url}/{post_id}")
        self._attach_details(response)
        return response
    
    def create(self, payload):
        response = requests.post(self.url, json=payload)
        self._attach_details(response)
        return response
    
    def get_all(self):
        response = requests.get(self.url)
        self._attach_details(response)
        return response

    
    def delete(self, post_id):
        response = requests.delete(f"{self.url}/{post_id}")
        self._attach_details(response)
        return response

    def update (self, post_id, payload):
        response = requests.put(f"{self.url}/{post_id}", json=payload)
        self._attach_details(response)
        return response
    
    def get_comments(self, post_id):
        response = requests.get(f"{self.url}/{post_id}/comments")
        self._attach_details(response)
        return response