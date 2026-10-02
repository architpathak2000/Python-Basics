import requests

def get_book():
    url = "https://api.freeapi.app/api/v1/public/books/book/random"
    response = requests.get(url) 
    data = response.json()
    # print(data)

    if data["success"] and "data" in data:
        message = data["message"]
        id = data["data"]["id"]
        title = data["data"]["volumeInfo"]["title"]
        return message,id,title
    else:
        raise Exception("Failed to fetch bookdata")
    
def main():
    try:
        message,id,title = get_book()
        print(f"MESSAGE: {message}\nID:{id}\nTITLE: {title}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()  