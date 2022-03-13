class NotSupportedEnv(Exception):
    """Raise when the env value is not supported."""
    pass


"""
Pass different values to a test function, depending on command line options
Przekaż różne wartości do funkcji testowej, w zależności od opcji wiersza poleceń
"""
class Config:
    """A config class allow customizing environment.
    Is useful for customizing test runs with the command line."""
    def __init__(self, env):

        SUPPORTED_ENVS = ['dev', 'qa'] # Supported environments

        """Simple validation of environment"""
        if env.lower() not in SUPPORTED_ENVS:
            raise NotSupportedEnv(f"{env} is not supported environment (supported envs: {SUPPORTED_ENVS})")

        """"""
        self.base_url = {'dev': 'https://mydev-env.com',
                         'qa': 'https://myqa-env.com'
                         }[env]

        """Simple example"""
        self.app_port = {
            'dev': 8080,
            'qa': 80
        }[env]