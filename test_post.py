import requests
import allure
import pytest
from jsonschema import validate
from schemas.post_schema import POST_SCHEMA

@allure.feature("Posts Management")
@allure.story("CRUD operations for posts")
class TestPosts:

    @allure.title("Test case #1: Get all posts")
    def test_get_all_posts(self, base_url):
        response = requests.get(f"{base_url}/posts")
        assert response.status_code == 200

    @allure.title("Test case #2: Get single post")
    def test_get_single_post(self, base_url):
        response = requests.get(f"{base_url}/posts/1")
        assert response.status_code == 200
        assert response.json()['id'] == 1

    @allure.title("Test case #3: Create a post")
    def test_create_post(self, base_url):
        payload = {"title": "AI Test", "body": "Clean code", "userId": 1}
        response = requests.post(f"{base_url}/posts", json=payload)
        assert response.status_code == 201
        assert response.json()['title'] == "AI Test"

    @allure.title("Test case #4: Update a post (PUT)")
    def test_update_post(self, base_url):
        payload = {"id": 1, "title": "Updated Title", "body": "Updated Body", "userId": 1}
        response = requests.put(f"{base_url}/posts/1", json=payload)
        assert response.status_code == 200
        assert response.json()['title'] == "Updated Title"

    @allure.title("Test case #5: Delete a post")
    def test_delete_post(self, base_url):
        response = requests.delete(f"{base_url}/posts/1")
        assert response.status_code == 200

    @allure.title("Test case #6: Parametrized title check")
    @pytest.mark.parametrize("title_value", ["Bug", "Task", "Story"])
    def test_parametrized_title(self, base_url, title_value):
        payload = {"title": title_value, "body": "Description", "userId": 1}
        response = requests.post(f"{base_url}/posts", json=payload)
        assert response.json()['title'] == title_value

    @allure.title("Test case #7: Check response structure")
    def test_structure(self, base_url):
        response = requests.get(f"{base_url}/posts/1")
        data = response.json()
        
        required_keys = ['userId', 'id', 'title', 'body']
        assert all(key in data for key in required_keys)

    @allure.title("Test case #8: Negative test - non-existent post")
    def test_get_non_existent_post(self, base_url):
        response = requests.get(f"{base_url}/posts/9999")
        assert response.status_code == 404