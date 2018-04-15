from flaskbb.utils.settings import FlaskBBConfig


def test_flaskbb_config(default_settings):
    flaskbb_config = FlaskBBConfig()

    assert len(flaskbb_config) > 0
    # test __getitem__
    assert flaskbb_config['PROJECT_TITLE'] == 'FlaskBB'
    # test __setitem__
    flaskbb_config['PROJECT_TITLE'] = 'FlaskBBTest'
    assert flaskbb_config['PROJECT_TITLE'] == 'FlaskBBTest'
    # test __iter__
    test_dict = {}
    assert type(flaskbb_config.__iter__()) == type(test_dict.__iter__())
