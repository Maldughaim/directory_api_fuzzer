import requests

def greating():
    option = int(input("1.Directory finder\n2.Api fuzzer\n0.exit\n"))

    if option == 0:
        exit(0)
    elif option == 1:
        dirFinder()
    elif option == 2:
        apiFuzzer()
    else:
        print("Invalid input")
        greating()

def dirFinder():
    burl = input("Enter target url: ")
    list = input("Enter the name of the directorys list file: ")
    try:
        with open(list) as f:
            for i in f:
                url = f'{burl}/{i.strip()}'
                try:
                    req = requests.get(url=url)
                except requests.exceptions.HTTPError as http_err:
                    print(f"HTTP error occurred: {http_err}")
                except requests.exceptions.RequestException as req_err:
                    print(f"An error occurred: {req_err}")
                
                if req.status_code != 404:
                    print(f'{url}   |   {req.status_code}')
    except FileNotFoundError:
        print(f"Error: File not found.")
    except Exception as e:
        print(f"An error occurred while opening the file: {e}")

def apiFuzzer():
    burl = input("Enter api url: ")
    list = input("Enter the name of the api endpoints list file: ")
    try:
        with open(list) as f:
            for i in f:
                url = f'{burl}/{i.strip()}'
                try:
                    req = requests.get(url=url)
                except requests.exceptions.HTTPError as http_err:
                    print(f"HTTP error occurred: {http_err}")
                except requests.exceptions.RequestException as req_err:
                    print(f"An error occurred: {req_err}")
            
                if req.status_code != 404 and req.headers.get('content-type', '') == 'application/json':
                    print(f'{url}   |   {req.status_code}')
                    print(req.json())
    except FileNotFoundError:
        print(f"Error: File not found.")
    except Exception as e:
        print(f"An error occurred while opening the file: {e}")

greating()
