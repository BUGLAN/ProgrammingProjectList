class BaseConfig:
    DEBUG = True


class TestConfig:
    DEBUG = True
    TESTING = True


class ProConfig:
    DEBUG = False


config = {'base': BaseConfig, 'pro': ProConfig, 'test': TestConfig}
