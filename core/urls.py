import importlib
import warnings


class Urls:

    def init_app(self, app, api):
        """
        加载配置中INSTALL_APP中的所有app的路由
        :param api: flask api 对象
        :param app: flask 应用对象
        :return:
        """
        apps = app.config.get("INSTALL_APPS")
        for application in apps:
            try:
                url_module = importlib.import_module("{0}.urls".format(application))
                if hasattr(url_module, "urlpatterns"):
                    urls = url_module.urlpatterns
                    for idx, url in enumerate(urls):
                        try:
                            api.add_resource(url[0], url[1])
                        except IndexError as e:
                            warnings.warn("app {0} urls index {1} format error!".format(application, idx + 1))
                else:
                    warnings.warn("app {0} urls not found attr urlpatterns".format(application))
            except ImportError as e:
                print(e)
                warnings.warn("app {0} not found module urls!".format(application))
