from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    @task
    def search(self):
        response = self.client.get("/")
        csrftoken = response.cookies['csrftoken']

        self.client.post("/", {
            "name": "Rio de Janeiro - Grand Court",
            "checkin": "2015-03-01",
            "checkout": "2015-04-01"},
            headers={"X-CSRFToken": csrftoken}
        )

    @task
    def search_two(self):
        response = self.client.get("/")
        csrftoken = response.cookies['csrftoken']

        self.client.post("/", {
            "name": "Rio de Janeiro - Grand",
            "checkin": "2015-01-01",
            "checkout": "2015-02-01"},
            headers={"X-CSRFToken": csrftoken}
        )


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 5000
