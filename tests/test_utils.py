
from utils import get_data


def test_get_data(test_url):
    assert len(get_data(test_url)[0]) > 0
    assert get_data('https://wrong.url.com/')[0] is None
    assert get_data('https://github.com/OGR41/coursework3.git')[0] is None
