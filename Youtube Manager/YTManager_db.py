import sqlite3
conn = sqlite3.connect("Youtube_videos.db")
cur = conn.cursor()

cur.execute('''  
    CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
    )
''')

def list_all_videos():
    cur.execute("SELECT * FROM videos")
    print("\n")
    print("*" * 70)

    for row in cur.fetchall():
        print(row)
    
    print("\n")
    print("*" * 70)

def add_videos():
    name = input("Enter Video Name : ")
    time = input("Enter Video Time : ")
    cur.execute("INSERT INTO videos(name,time) VALUES (?,?)",(name,time))
    conn.commit()

def update_video():
    list_all_videos()
    video_id = int(input("Enter video id to update : "))
    name = input("Enter Video Name : ")
    time = input("Enter Video Time : ")
    cur.execute('''
                UPDATE VIDEOS SET name = ?,time=? where id = ?
                ''',(name,time,video_id))

def delete_video():
    list_all_videos()
    video_id = int(input("Enter video id to delete : "))
    cur.execute("DELETE FROM VIDEOS WHERE id = ?",(video_id,))
    conn.commit()


def main():
    while True:

        print("\nYoutbe Manager  | Choose your option")
        print('\n1.List all videos')
        print('\n2.Add a youtube video')
        print('\n3.Update a youtube video')
        print('\n4.Delete a youtube video')
        print('\n5.Exit the App\n')        

        choice = input("Enter your choice : ")

        match choice:
            case '1': list_all_videos()
            case '2': add_videos()
            case '3': update_video()
            case '4': delete_video()
            case '5': break
            case _: print("Invalid Input")
    conn.close()
    

if __name__ == "__main__":
    main()