

class TestQaEnv:
    def test_environment_is_qa(self, env):
        assert env == 'qa'

    def test_environment_base_url(self, app_config):
        assert app_config.base_url == 'https://myqa-env.com'

    def test_environment_app_port(self, app_config):
        assert app_config.app_port == 80


class TestDevEnv:
    def test_environment_is_dev(self, env):
        assert env == 'dev'

    def test_environment_base_url(self, app_config):
        assert app_config.base_url == 'https://mydev-env.com'

    def test_environment_app_port(self, app_config):
        assert app_config.app_port == 8080

