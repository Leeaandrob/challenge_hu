from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    @task
    def search(self):
        response = self.client.get("/")
        csrftoken = response.cookies['csrftoken']

        self.client.post("/", {
            "name": "Nova Friburgo - Grand Uysal",
            "available": True,
            "checkin": "2015-05-01",
            "checkout": "2015-05-30"},
            headers={"X-CSRFToken": csrftoken}
        )

    @task
    def search_two(self):
        response = self.client.get("/")
        csrftoken = response.cookies['csrftoken']

        self.client.post("/", {
            "name": "Rio Claro - Charisma Deluxe",
            "available": True,
            "checkin": "2015-05-01",
            "checkout": "2015-05-30"},
            headers={"X-CSRFToken": csrftoken}
        )


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 5000
