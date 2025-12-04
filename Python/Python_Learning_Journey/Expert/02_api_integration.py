"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                              Kataria Kushal                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝

Program 2: API Integration and HTTP Requests
Learning Objective: Learn to interact with web APIs and handle HTTP requests
"""

import json
import time
from urllib.parse import urlencode
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

# Note: This example uses urllib (built-in) instead of requests library
# In real projects, consider using the 'requests' library for easier API handling

# Basic HTTP GET request
print("=== Basic HTTP GET Request ===")

def make_get_request(url):
    """Make a simple GET request"""
    try:
        with urlopen(url) as response:
            data = response.read().decode('utf-8')
            return json.loads(data)
    except HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
        return None
    except URLError as e:
        print(f"URL Error: {e.reason}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        return None

# Example with JSONPlaceholder API (free testing API)
api_url = "https://jsonplaceholder.typicode.com/posts/1"
post_data = make_get_request(api_url)

if post_data:
    print(f"Post Title: {post_data['title']}")
    print(f"Post Body: {post_data['body'][:50]}...")

# HTTP POST request
print("\n=== HTTP POST Request ===")

def make_post_request(url, data):
    """Make a POST request with JSON data"""
    try:
        # Convert data to JSON
        json_data = json.dumps(data).encode('utf-8')
        
        # Create request with headers
        request = Request(url, data=json_data)
        request.add_header('Content-Type', 'application/json')
        request.add_header('User-Agent', 'Python-API-Client/1.0')
        
        with urlopen(request) as response:
            response_data = response.read().decode('utf-8')
            return json.loads(response_data)
    
    except Exception as e:
        print(f"POST Request Error: {e}")
        return None

# Create a new post
new_post = {
    "title": "My New Post",
    "body": "This is the content of my new post",
    "userId": 1
}

post_url = "https://jsonplaceholder.typicode.com/posts"
created_post = make_post_request(post_url, new_post)

if created_post:
    print(f"Created post with ID: {created_post['id']}")
    print(f"Title: {created_post['title']}")

# API with query parameters
print("\n=== API with Query Parameters ===")

def get_posts_by_user(user_id):
    """Get posts by a specific user"""
    base_url = "https://jsonplaceholder.typicode.com/posts"
    params = {"userId": user_id}
    
    # Build URL with query parameters
    query_string = urlencode(params)
    full_url = f"{base_url}?{query_string}"
    
    return make_get_request(full_url)

user_posts = get_posts_by_user(1)
if user_posts:
    print(f"User 1 has {len(user_posts)} posts")
    for post in user_posts[:3]:  # Show first 3 posts
        print(f"- {post['title']}")

# API Client Class
print("\n=== API Client Class ===")

class JSONPlaceholderClient:
    """API client for JSONPlaceholder service"""
    
    def __init__(self, base_url="https://jsonplaceholder.typicode.com"):
        self.base_url = base_url
        self.session_headers = {
            'User-Agent': 'Python-API-Client/1.0',
            'Accept': 'application/json'
        }
    
    def _make_request(self, method, endpoint, data=None):
        """Make HTTP request with error handling"""
        url = f"{self.base_url}/{endpoint}"
        
        try:
            if method == "GET":
                request = Request(url)
            elif method == "POST":
                json_data = json.dumps(data).encode('utf-8') if data else None
                request = Request(url, data=json_data)
                request.add_header('Content-Type', 'application/json')
            
            # Add session headers
            for header, value in self.session_headers.items():
                request.add_header(header, value)
            
            with urlopen(request) as response:
                response_data = response.read().decode('utf-8')
                return json.loads(response_data)
        
        except Exception as e:
            print(f"Request failed: {e}")
            return None
    
    def get_posts(self, user_id=None):
        """Get posts, optionally filtered by user"""
        endpoint = "posts"
        if user_id:
            endpoint += f"?userId={user_id}"
        return self._make_request("GET", endpoint)
    
    def get_post(self, post_id):
        """Get a specific post"""
        return self._make_request("GET", f"posts/{post_id}")
    
    def create_post(self, title, body, user_id):
        """Create a new post"""
        data = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        return self._make_request("POST", "posts", data)
    
    def get_users(self):
        """Get all users"""
        return self._make_request("GET", "users")

# Using the API client
client = JSONPlaceholderClient()

# Get a specific post
post = client.get_post(5)
if post:
    print(f"Post 5 title: {post['title']}")

# Get users
users = client.get_users()
if users:
    print(f"Found {len(users)} users:")
    for user in users[:3]:
        print(f"- {user['name']} ({user['email']})")

# Rate limiting and retry logic
print("\n=== Rate Limiting and Retry Logic ===")

class RateLimitedClient:
    """API client with rate limiting and retry logic"""
    
    def __init__(self, requests_per_second=1):
        self.min_interval = 1.0 / requests_per_second
        self.last_request_time = 0
    
    def make_request_with_retry(self, url, max_retries=3):
        """Make request with rate limiting and retry logic"""
        for attempt in range(max_retries):
            try:
                # Rate limiting
                current_time = time.time()
                time_since_last = current_time - self.last_request_time
                if time_since_last < self.min_interval:
                    sleep_time = self.min_interval - time_since_last
                    print(f"Rate limiting: sleeping for {sleep_time:.2f} seconds")
                    time.sleep(sleep_time)
                
                # Make request
                with urlopen(url) as response:
                    self.last_request_time = time.time()
                    data = response.read().decode('utf-8')
                    return json.loads(data)
            
            except HTTPError as e:
                if e.code == 429:  # Too Many Requests
                    wait_time = 2 ** attempt  # Exponential backoff
                    print(f"Rate limited. Waiting {wait_time} seconds before retry {attempt + 1}")
                    time.sleep(wait_time)
                else:
                    print(f"HTTP Error {e.code}: {e.reason}")
                    break
            
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt < max_retries - 1:
                    time.sleep(1)
        
        return None

# Test rate-limited client
rate_limited_client = RateLimitedClient(requests_per_second=0.5)  # 1 request per 2 seconds

urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3"
]

for url in urls:
    result = rate_limited_client.make_request_with_retry(url)
    if result:
        print(f"Successfully fetched: {result['title']}")

# Mock API for testing
print("\n=== Mock API Response ===")

def mock_api_response(endpoint, method="GET"):
    """Mock API responses for testing"""
    mock_data = {
        "posts": [
            {"id": 1, "title": "Mock Post 1", "body": "Mock content 1"},
            {"id": 2, "title": "Mock Post 2", "body": "Mock content 2"}
        ],
        "users": [
            {"id": 1, "name": "Mock User", "email": "mock@example.com"}
        ]
    }
    
    print(f"Mock API call: {method} /{endpoint}")
    return mock_data.get(endpoint, {"error": "Endpoint not found"})

# Test with mock data
mock_posts = mock_api_response("posts")
print(f"Mock posts: {len(mock_posts)} items")

"""
Example Output:
=== Basic HTTP GET Request ===
Post Title: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
Post Body: quia et suscipit suscipit recusandae consequuntur...

=== HTTP POST Request ===
Created post with ID: 101
Title: My New Post

=== API with Query Parameters ===
User 1 has 10 posts
- sunt aut facere repellat provident occaecati excepturi optio reprehenderit
- qui est esse
- ea molestias quasi exercitationem repellat qui ipsa sit aut

=== API Client Class ===
Post 5 title: nesciunt quas odio
Found 10 users:
- Leanne Graham (Sincere@april.biz)
- Ervin Howell (Shanna@melissa.tv)
- Clementine Bauch (Nathan@yesenia.net)

What you learned:
- Making HTTP GET and POST requests with urllib
- Handling JSON data and API responses
- Error handling for network requests
- Building URLs with query parameters
- Creating reusable API client classes
- Rate limiting and retry logic for robust API calls
- Mock API responses for testing
- Best practices for API integration
- Authentication headers and request customization
"""