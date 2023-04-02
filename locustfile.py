from locust import HttpUser, task


class HelloWorldUser(HttpUser):

    @task
    def slash(self):
        self.client.get("/")

    @task
    def hello(self):
        self.client.get("/hello")
