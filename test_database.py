from database import Video
import os # remove database file once done each test

# Tests to see if database can be created, then pass if so
def test_init():
    db = Video("test.db") 
    os.remove("test.db")
    pass
     
# Tests to see if insertion is possible, then pass if so
def test_insert_six():
    db = Video("test.db")
    db.insert_six("Test_SD","Test_480p","Test_4:3",
        "Test_640x480","Test_100MB",
        "Test_/videos/video1-sd.mkv")
    os.remove("test.db")
    pass

def test_search():
    db = Video("test.db")
    db.insert_six("Test_SD","Test_480p","Test_4:3",
        "Test_640x480","Test_100MB",
        "Test_/videos/video1-sd.mkv")
    test_sd_search_res = db.search_column("Test_SD")
    assert str(test_sd_search_res.fetchall()) == "[('Test_SD', 'Test_480p', 'Test_4:3', 'Test_640x480', 'Test_100MB', 'Test_/videos/video1-sd.mkv')]"
    os.remove("test.db")

