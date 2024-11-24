
import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []

def save_video_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)


def list_all_videos(videos):
    print("\n")
    print("*" * 160)
    for index, vid in enumerate(videos, start=1):
        print(f"{index}. {vid['name']}, Duration: {vid['time']}")
    print("\n")
    print("*" * 160)

def add_video(videos):
    name = input("Enter name of the video: ")
    time = int(input("Enter time of the video: "))
    videos.append({'name': name, 'time': time})
    save_video_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter video number which you want to update: "))
    if 1 <= index <= len(videos): 
        name = input("Enter name of the video: ")
        time = int(input("Enter time of the video: "))
        videos[index-1] = {'name': name, 'time': time}
        save_video_helper(videos)
    else:
        print("Invalid number")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter video number which you want to delete: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_video_helper(videos)
    else:
        print("Invalid number")
    
    

def main():
    videos = load_data()
    while True:
        print("Youtube manager app")
        print("1. List all youtube videos")
        print("2. Add youtube video")
        print("3. Update youtube video")
        print("4. Delete youtube video")
        print("5. Exit app")
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                list_all_videos(videos)
            case 2:
                add_video(videos)
            case 3:
                update_video(videos)
            case 4:
                delete_video(videos)
            case 5:
                break
            case _:
                print("Invalid choice")

if __name__ == '__main__':
    main()