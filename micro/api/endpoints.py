from celery import Celery

app = Celery("Micro", backend="amqp://")


class Request:
    @staticmethod
    def credentials(broker, queue):
        app.conf.update(
            broker_url=broker,
            task_routes={"Micro.*": {"queue": queue}}
        )

    @staticmethod
    @app.task(name="Micro.plugins")
    def plugins():
        pass

    @staticmethod
    @app.task(name="Micro.info")
    def info(name):
        pass

    @staticmethod
    @app.task(name="Micro.help")
    def help(name):
        pass

    @staticmethod
    @app.task(name="Micro.run")
    def run(plugin_name, **kwargs):
        pass

