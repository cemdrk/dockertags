import src
from src.__main__ import main


def test_image_name_argument(capfd, monkeypatch):
    image_name = "python"

    def mock_fetch(*args, **kwargs):
        return {"results": [{"name": "latest"}]}

    monkeypatch.setattr(src.__main__, "fetch_json_from_url", mock_fetch)

    main([image_name])

    out, err = capfd.readouterr()
    assert err == ""
    assert out == "python:latest\n"
