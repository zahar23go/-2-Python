import requests

class ProjectAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, title, users=None):
        data = {"title": title}
        if users:
            data["users"] = users
        response = requests.post(
            f"{self.base_url}/projects",
            headers=self.headers,
            json=data
        )
        return response

    def get_project(self, project_id):
        response = requests.get(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers
        )
        return response

    def update_project(self, project_id, title=None, users=None):
        data = {}
        if title:
            data["title"] = title
        if users:
            data["users"] = users
        response = requests.put(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers,
            json=data
        )
        return response