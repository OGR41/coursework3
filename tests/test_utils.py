from utils import get_data, get_filter_data


def test_get_data(url='https://www.sky.pro'):
    assert len(get_data(url)) > 0
    assert get_data('https://wrong.url.com/')[0] is None
    assert get_data('https://github.com/OGR41/coursework3.git')[0] is None
    assert get_data('https://github.com/OGR41/course/work3.git')[0] is None


def test_get_filter_data(test_data):
    assert len(get_filter_data(test_data)) == 4

