import json
from pathlib import Path

FILE_PATH = Path(__file__).parent / "youtube.txt"

def load_data():
    try:
        with open(FILE_PATH,'r')as file:
            return json.load(file)
    except (FileNotFoundError ,json.JSONDecodeError ):
        return[]

def savedata_helper(videos):
    with open(FILE_PATH,'w') as file:
        json.dump(videos,file)

def list_all_videos(videos):
    print("\n")
    print("*" * 70)

    for index,video in enumerate(videos,start=1):
        print(F"{index}.{video['Name']},Duration{video['Time']}")

    print("\n")
    print("*" * 70)

def add_videos(videos):
    name = input("Enter the name of video : ")
    time = input("Enter the time of video : ")

    videos.append({'Name':name,'Time':time})
    savedata_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of video to be updated: "))

    if 1 <= index <= len(videos):
        name = input("Enter name of video : ")
        time = input("Enter time of video : ")
        videos[index-1] = {'Name':name,'Time':time}
        savedata_helper(videos)

    else:
        print("\n")
        print("*" * 70)

        print("INVALID INDEX ENTERED")

        print("\n")
    print("*" * 70)

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of video to be Deleted: "))

    if 1 <= index <= len(videos):
        del(videos[index-1])
        savedata_helper(videos)

    else:
        print("\n")
        print("*" * 70)

        print("INVALID INDEX ENTERED")

        print("\n")
    print("*" * 70)

def main():
    videos = load_data()

    while True:

        print("\nYoutbe Manager  | Choose your option")
        print('\n1.List all videos')
        print('\n2.Add a youtube video')
        print('\n3.Update a youtube video')
        print('\n4.Delete a youtube video')
        print('\n5.Exit the App\n')        

        choice = input("Enter your choice : ")

        match choice:
            case '1': list_all_videos(videos)
            case '2': add_videos(videos)
            case '3': update_video(videos)
            case '4': delete_video(videos)
            case '5': break
            case _: print("Invalid Input")

if __name__ == "__main__":
    main()
