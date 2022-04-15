from src.__main__ import main


def test_image_name_argument():
    image_name = "python"
    assert main([image_name]) == image_name
