
import datetime
import json
import os
import requests

PIXELA_ENDPOINT : str = "https://pixe.la/v1/users"

os.environ["PIXELA_TOKEN"] = "+*a3&Q4t+(a%1*2mLJ2$x$(&#v%j!%jR*hg!2M577S$Jy(90*33Y$Q42+37n3$O8XW&d825%4*+38N)V)z$5J319L40Z3$06$*o4CK&$K"
os.environ["PIXELA_USERNAME"] = "giacconidev"

def load_response_in_json(r) :
    my_json = r.decode('utf8').replace("'", '"')
    return json.loads(my_json)
    

user_creation_params : object = {
    "token": os.environ["PIXELA_TOKEN"],
    "username": os.environ["PIXELA_USERNAME"],
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
 }

graph_creation_params : object = {
    "id": "habit-01",
    "name": "udemy daily videos completed",
    "unit": "videos completed",
    "type": "int",
    "color": "ajisai"
 }

graph_pixel_addition_params : object = {
    "id": "habit-01",
    "name": "udemy daily videos completed",
    "unit": "videos completed",
    "type": "int",
    "color": "ajisai"
 }

graph_headers = {
    "X-USER-TOKEN": os.environ["PIXELA_TOKEN"]
}

# response_create = requests.post(PIXELA_ENDPOINT, json=user_creation_params)
# body = response_create.json()

# if response_create.ok:
#     print("User created successfully")
#     print(json.dumps(body, indent=1))
# else:
#     print("Oh no, a wild error appeared!")
#     print(json.dumps(body, indent=1))

response_add_graph = requests.post(f"{PIXELA_ENDPOINT}/{os.environ['PIXELA_USERNAME']}/graphs", json=graph_creation_params, headers=graph_headers)

if response_add_graph.ok:
    print("Graph created successfully")
else:
    if response_add_graph.status_code == 404:
        print(f"Oh no, a wild error appeared!: \n 404")
    else:
        content = load_response_in_json(response_add_graph.content)
        print(f"Oh no, a wild error appeared!: \n {content['message']}")
        

def add_todays_pixel():
    response_add_pixel = requests.post(f"{PIXELA_ENDPOINT}/{os.environ['PIXELA_USERNAME']}/graphs/{graph_creation_params['id']}", json=graph_pixel_addition_params, headers=graph_headers)
    if response_add_pixel.ok:
        print("Graph created successfully")
    else:
        if response_add_pixel.status_code == 404:
            print(f"Oh no, a wild error appeared!: \n 404")
        else:
            content = load_response_in_json(response_add_pixel.content)
            print(f"Oh no, a wild error appeared!: \n {content['message']}")
            # resent in case of intentional error due not supporter
            if "rejected 25%" in content['message']:
                add_todays_pixel();
                    
def update_pixel():
    response_update_pixel = requests.put(f"{PIXELA_ENDPOINT}/{os.environ['PIXELA_USERNAME']}/graphs/{graph_creation_params['id']}/{graph_pixel_addition_params['date']}", json=graph_pixel_addition_params, headers=graph_headers)
    if response_update_pixel.ok:
        print("Pixel updated successfully")
    else:
        if response_update_pixel.status_code == 404:
            print(f"Oh no, a wild error appeared!: \n 404")
        else:
            content = load_response_in_json(response_update_pixel.content)
            print(f"Oh no, a wild error appeared!: \n {content['message']}")
            # resent in case of intentional error due not supporter
            if "rejected 25%" in content['message']:
                update_pixel();
                    
                    
def delete_pixel():
    response_delete_pixel = requests.delete(f"{PIXELA_ENDPOINT}/{os.environ['PIXELA_USERNAME']}/graphs/{graph_creation_params['id']}/{graph_pixel_addition_params['date']}", json=graph_pixel_addition_params, headers=graph_headers)
    if response_delete_pixel.ok:
        print("Pixel deleted successfully")
    else:
        if response_delete_pixel.status_code == 404:
            print(f"Oh no, a wild error appeared!: \n 404")
        else:
            content = load_response_in_json(response_delete_pixel.content)
            print(f"Oh no, a wild error appeared!: \n {content['message']}")
            # resent in case of intentional error due not supporter
            if "rejected 25%" in content['message']:
                delete_pixel();
            
quant = input("Select quantity to add as a pixel for today!")
# yyyyMMdd format data
todays_date = datetime.date.today()
graph_pixel_addition_params["quantity"] = quant
graph_pixel_addition_params["date"] = todays_date.strftime("%Y%m%d")
add_todays_pixel()

#graph_pixel_addition_params["quantity"] = "7"
update_pixel()

#delete_pixel()
