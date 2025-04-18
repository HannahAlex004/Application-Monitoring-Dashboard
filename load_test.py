import requests 
import time 
import random 
 
API_BASE = "http://localhost:8000" 
GET_ENDPOINTS = [ 
    "/", 
    "/users/1", 
    "/products/101", 
    "/slow-endpoint", 
    "/error-test",
] 

POST_ENDPOINTS = ["/users",]


 
def simulate_traffic(): 
    while True: 
        method=random.choice(["GET", "POST"])
        if method == "GET": 
            endpoint = random.choice(GET_ENDPOINTS) 
            try: 
                response = requests.get(f"{API_BASE}{endpoint}") 
                print(f"Hit {endpoint} â†’ Status: {response.status_code}") 
            except Exception as e: 
                print(f"Error on {endpoint}: {e}") 
        else: 
            endpoint = random.choice(GET_ENDPOINTS) 
            data = {"name": f"User{random.randint(1, 100)}"} 
            try: 
                response = requests.post(f"{API_BASE}{endpoint}", json=data) 
                print(f"Hit {endpoint} â†’ Status: {response.status_code}") 
            except Exception as e: 
                print(f"Error on {endpoint}: {e}")
        endpoint = random.choice(POST_ENDPOINTS) 
        try: 
            response = requests.get(f"{API_BASE}{endpoint}") 
            print(f"Hit {endpoint} â†’ Status: {response.status_code}") 
        except Exception as e: 
            print(f"Error on {endpoint}: {e}") 
        time.sleep(random.uniform(0.1, 1.0)) 
 
if __name__ == "__main__": 
    simulate_traffic()
