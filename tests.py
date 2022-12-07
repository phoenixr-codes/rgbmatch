import pytest
import rgbmatch

def test_closest_color():
    assert rgbmatch.closest_rgb(
        (0,0,0),
        [
            (95,110,5),
            (4,4,4),
            (100,100,100)
        ]
    ) == (4,4,4)
    
    assert rgbmatch.closest_rgb(
        (0,0,0),
        [
            (95,110,5),
            (0,0,0),
            (100,100,100)
        ]
    ) == (0,0,0)
    
    with pytest.raises(RuntimeError):
        rgbmatch.closest_rgb((0,0,0), [])

