import sqlite3

class Video:
    def __init__(self, database_name):
        self.db = sqlite3.connect(database_name) # Connect to database
        self.cursor = self.db.cursor() # Create cursor
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS 
            videos(Resolution, Name, Aspect_Ratio, 
                   Pixel_Size, File_Size, File_Location)""")
        self.db.commit() 

    def insert_six(self, resolution, name, aspect_ratio, 
               pixel_size, file_size, file_location):
        self.cursor.execute("""INSERT INTO videos VALUES
            (?,?,?,?,?,?)
        """, (resolution, name, aspect_ratio, pixel_size,
              file_size, file_location))
        self.db.commit()

    def search_column(self, column):
        #return self.cursor.execute("SELECT (?) FROM videos", (column,))
        return self.cursor.execute("""
            SELECT * FROM videos where Resolution = (?)""", (column,))

def main():
    videos = Video("videos.db") # Create Video object
    # Some examples on how to run these python methods
    videos.insert_six("SD","480p","4:3","640x480","100MB","/videos/video1-sd.mkv")
    videos.insert_six("SD","480p","4:3","640x480","100MB","/videos/video2-sd.mkv")
    videos.insert_six("HD","720p","16:9","1280x720","300MB","/videos/video2-hd.mkv")
    res = videos.search_column("SD") 
    print(res.fetchall()) # prints result of everything that matched with SD

if __name__ == "__main__":
    main()
