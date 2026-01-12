import allure
import pytest
from jsonschema import validate
from schemas.post_schema import POST_SCHEMA
from api_client import PostClient


@allure.feature("Posts Management")
@allure.story("CRUD operations for posts")
class TestPosts:
    client = PostClient()

    @allure.title("Test case #1: Get all posts")
    def test_get_all_posts(self):
        response = self.client.get_all()
        assert response.status_code == 200

    @allure.title("Test case #2: Get single post")
    def test_get_single_post(self):
        response = self.client.get_one(1)
        assert response.status_code == 200
        assert response.json()['id'] == 1

    @allure.title("Test case #3: Create a post")
    def test_create_post(self):
        payload = {"title": "AI Test", "body": "Clean code", "userId": 1}
        response = self.client.create(payload)
        assert response.status_code == 201
        assert response.json()['title'] == "AI Test"

    @allure.title("Test case #4: Update a post (PUT)")
    def test_update_post(self):
        payload = {"id": 1, "title": "Updated Title", "body": "Updated Body", "userId": 1}
        response = self.client.update(1, payload)
        assert response.status_code == 200
        assert response.json()['title'] == "Updated Title"

    @allure.title("Test case #5: Delete a post")
    def test_delete_post(self):
        response = self.client.delete(1)
        assert response.status_code == 200

    @allure.title("Test case #6: Parametrized title check")
    @pytest.mark.parametrize("title_value", ["Bug", "Task", "Story"])
    def test_parametrized_title(self, title_value):
        payload = {"title": title_value, "body": "Description", "userId": 1}
        response = self.client.create(payload)
        assert response.json()['title'] == title_value

    @allure.title("Test case #7: Check response structure")
    def test_structure(self):
        response = self.client.get_one(1)
        data = response.json()
        
        required_keys = ['userId', 'id', 'title', 'body']
        assert all(key in data for key in required_keys)

    @allure.title("Test case #8: Negative test - non-existent post")
    def test_get_non_existent_post(self):
        response = self.client.get_one(9999)
        assert response.status_code == 404