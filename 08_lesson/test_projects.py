from ProjectAPI import ProjectAPI

class TestProjects:
    def test_create_project_positive(self, base_url, auth_token):
        api = ProjectAPI(base_url, auth_token)
        response = api.create_project("Тестовый проект")
        assert response.status_code == 201
        data = response.json()
        assert "id" in data
        project_id = data["id"]
        get_response = api.get_project(project_id)
        assert get_response.status_code == 200
        assert get_response.json()["title"] == "Тестовый проект"

    def test_create_project_negative_empty_title(self, base_url, auth_token):
        api = ProjectAPI(base_url, auth_token)
        response = api.create_project("")
        assert response.status_code == 400

    def test_get_project_positive(self, base_url, auth_token):
        api = ProjectAPI(base_url, auth_token)
        create_response = api.create_project("Проект для GET теста")
        assert create_response.status_code == 201
        project_id = create_response.json()["id"]
        get_response = api.get_project(project_id)
        assert get_response.status_code == 200
        data = get_response.json()
        assert data["id"] == project_id
        assert data["title"] == "Проект для GET теста"

    def test_get_project_negative_not_found(self, base_url, auth_token):
        api = ProjectAPI(base_url, auth_token)
        response = api.get_project("non-existent-id-12345")
        assert response.status_code == 404

    def test_update_project_positive(self, base_url, auth_token):
        api = ProjectAPI(base_url, auth_token)
        create_response = api.create_project("Старое название")
        assert create_response.status_code == 201
        project_id = create_response.json()["id"]
        update_response = api.update_project(project_id, title="Новое название")
        assert update_response.status_code == 200
        get_response = api.get_project(project_id)
        assert get_response.status_code == 200
        assert get_response.json()["title"] == "Новое название"

    def test_update_project_negative_invalid_id(self, base_url, auth_token):
        api = ProjectAPI(base_url, auth_token)
        response = api.update_project("invalid-id", title="Новое название")
        assert response.status_code == 404