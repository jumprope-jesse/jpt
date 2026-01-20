---
type: link
source: notion
url: https://rednafi.com/misc/etag_and_http_caching/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-04-11T00:26:00.000Z
---

# ETag and HTTP caching | Redowan's Reflections

## Overview (from Notion)
- Efficiency and Performance: Understanding ETags and HTTP caching can help optimize web applications, reducing load times and server requests—crucial for maintaining user engagement in a fast-paced digital environment.

- Family Time: Efficient caching means less waiting around for pages to load, allowing more quality time with family or pursuing personal interests.

- Tech Savvy: As a founder, leveraging caching strategies can set your product apart, showcasing your commitment to performance and user experience.

- Resource Management: Insight into HTTP caching can help you make informed decisions about server architecture and resource allocation, essential for a startup's budget.

- New York City's Fast Pace: In a bustling city, speed is everything. Understanding these concepts can help your applications perform well in a competitive market.

- Alternative Perspectives: Some argue that over-optimization can lead to complexity. Balancing simplicity and performance is key—don’t sacrifice maintainability for speed.

- Continuous Learning: The tech landscape evolves quickly. Staying updated on topics like ETags fosters a growth mindset, which is vital for personal and professional development.

## AI Summary (from Notion)
The HTTP ETag header is useful for client-side caching of GET requests, allowing clients to cache responses and validate them with the server using If-None-Match. If the ETag matches, the server responds with 304 Not Modified, saving bandwidth. A Go server example demonstrates generating weak ETags and handling conditional requests. Consistency of ETags across servers is crucial to prevent unnecessary data transfers and improve caching efficiency.

## Content (from Notion)

One neat use case for the HTTP ETag header is client-side HTTP caching for GET requests. Along with the ETag header, the caching workflow requires you to fiddle with other conditional HTTP headers like If-Match or If-None-Match. However, their interaction can feel a bit confusing at times.

Every time I need to tackle this, I end up spending some time browsing through the relevant MDN docs123 to jog my memory. At this point, I’ve done it enough times to justify spending the time to write this.

## Caching the response of a GET endpoint

The basic workflow goes as follows:

- The client makes a GET request to the server.
- The server responds with a 200 OK status, including the content requested and an ETag header.
- The client caches the response and the ETag value.
- For subsequent requests to the same resource, the client includes the If-None-Match header with the ETag value it has cached.
- The server regenerates the ETag independently and checks if the ETag value sent by the client matches the generated one.
```plain text
Client                                 Server
  |                                       |
  |----- GET Request -------------------->|
  |                                       |
  |<---- Response 200 OK + ETag ----------|
  |     (Cache response locally)          |
  |                                       |
  |----- GET Request + If-None-Match ---->|  (If-None-Match == previous ETag)
  |                                       |
  |       Does ETag match?                |
  |<---- Yes: 304 Not Modified -----------|  (No body sent; Use local cache)
  |       No: 200 OK + New ETag ----------|  (Update cached response)
  |                                       |

```

We can test this workflow with GitHub’s REST API suite via the GitHub CLI4. If you’ve installed the CLI and authenticated yourself, you can make a request like this:

```plain text
gh api -i  /users/rednafi

```

This asks for the data associated with the user rednafi. The response looks as follows:

```plain text
HTTP/2.0 200 OK
Etag: W/"b8fdfabd59aed6e0e602dd140c0a0ff48a665cac791dede458c5109bf4bf9463"
{
  "login":"rednafi",
  "id":30027932,
  ...
}

```

I’ve truncated the response body and omitted the headers that aren’t relevant to this discussion. You can see that the HTTP status code is 200 OK and the server has included an ETag header.

The W/ prefix indicates that a weak validator5 is used to validate the content of the cache. Using a weak validator means when the server compares the response payload to generate the hash, it doesn’t do it bit-by-bit. So, if your response is JSON, then changing the format of the JSON won’t change the value of the ETag header since two JSON payloads with the same content but with different formatting are semantically the same thing.

Let’s see what happens if we make the same request again while passing the value of the ETag in the If-None-Match header.

```plain text
gh api -i -H \
    'If-None-Match: W/"b8fdfabd59aed6e0e602dd140c0a0ff48a665cac791dede458c5109bf4bf9463"' \
    /users/rednafi

```

This returns:

```plain text
HTTP/2.0 304 Not Modified
Etag: "b8fdfabd59aed6e0e602dd140c0a0ff48a665cac791dede458c5109bf4bf9463"
gh: HTTP 304

```

This means that the cached response in the client is still valid and it doesn’t need to refetch that from the server. So, the client can be coded to serve the previously cached data to the users when asked for.

A few key points to keep in mind:

- Always wrap your ETag values in double quotes when sending them with the If-None-Match header, just as the spec says6.
- Using the If-None-Match header to pass the ETag value means that the client request is considered successful when the ETag value from the client doesn’t match that of the server. When the values match, the server will return 304 Not Modified with no body.
- If we’re writing a compliant server, when it comes to If-None-Match, the spec tells us7 to use a weak comparison for ETags. This means that the client will still be able to validate the cache with weak ETags, even if there have been slight changes to the representation of the data.
- If the client is a browser, it’ll automatically manage the cache and send conditional requests without any extra work.
## Writing a server that enables client-side caching

If you’re serving static content, you can configure your load balancer to enable this caching workflow. But for dynamic GET requests, the server needs to do a bit more work to allow client-side caching.

Here’s a simple server in Go that enables the above workflow for a dynamic GET request:

```plain text
package main
import (
    "crypto/sha256"
    "encoding/hex"
    "fmt"
    "net/http"
    "strings"
)
// calculateETag generates a weak ETag by SHA-256-hashing the content
// and prefixing it with W/ to indicate a weak comparison
func calculateETag(content string) string {
    hasher := sha256.New()
    hasher.Write([]byte(content))
    hash := hex.EncodeToString(hasher.Sum(nil))
    return fmt.Sprintf("W/\"%s\"", hash)
}
func main() {
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        // Define the content within the handler
        content := `{"message": "Hello, world!"}`
        eTag := calculateETag(content)
        // Remove quotes and W/ prefix for If-None-Match header comparison
        ifNoneMatch := strings.TrimPrefix(
            strings.Trim(r.Header.Get("If-None-Match"), "\""), "W/")
        // Generate a hash of the content without the W/ prefix for comparison
        contentHash := strings.TrimPrefix(eTag, "W/")
        // Check if the ETag matches; if so, return 304 Not Modified
        if ifNoneMatch == strings.Trim(contentHash, "\"") {
            w.WriteHeader(http.StatusNotModified)
            return
        }
        // If ETag does not match, return the content and the ETag
        w.Header().Set("ETag", eTag) // Send weak ETag
        w.Header().Set("Content-Type", "application/json")
        w.WriteHeader(http.StatusOK)
        fmt.Fprint(w, content)
    })
    fmt.Println("Server is running on http://localhost:8080")
    http.ListenAndServe(":8080", nil)
}

```

- The server generates a weak ETag for its content by creating a SHA-256 hash and adding W/ to the front, indicating it’s meant for weak comparison.
- When delivering content, the server includes this weak ETag in the response headers, allowing clients to cache the content along with the ETag.
- For subsequent requests, the server checks if the client has sent an ETag in the If-None-Match header and weakly compares it with the current content’s ETag by independently generating the hash.
- If the ETags match, indicating no significant content change, the server replies with a 304 Not Modified status. Otherwise, it sends the content again with a 200 OK status and updates the ETag. When this happens, the client knows that the existing cache is still warm and can be served without any changes to it.
You can run the server by running go run main.go and from a different console start making requests to it like this:

```plain text
curl -i  http://localhost:8080/foo

```

This will return the ETag header along with the JSON response:

```plain text
HTTP/1.1 200 OK
Content-Type: application/json
Etag: W/"1d3b4242cc9039faa663d7ca51a25798e91fbf7675c9007c2b0470b72c2ed2f3"
Date: Wed, 10 Apr 2024 15:54:33 GMT
Content-Length: 28
{"message": "Hello, world!"}

```

Now, you can make another request with the value of

the ETag in the If-None-Match header:

```plain text
curl -i -H \
    'If-None-Match: "1d3b4242cc9039faa663d7ca51a25798e91fbf7675c9007c2b0470b72c2ed2f3"' \
    http://localhost:8080/foo

```

This will return a 304 Not Modified response with no body:

```plain text
HTTP/1.1 304 Not Modified
Date: Wed, 10 Apr 2024 15:57:25 GMT

```

In a real-life scenario, you’ll probably factor out the caching part in middleware so that all of your HTTP GET requests can be cached from the client-side without repetition.

## One thing to look out for

While writing a cache-enabled server, make sure the system is set up so that the server always sends back the same ETag for the same content, even when there are multiple servers working behind a load balancer. If these servers give out different ETags for the same content, it can mess up how clients cache that content.

Clients use ETags to decide if content has changed. If the ETag value hasn’t changed, they know the content is the same and don’t download it again, saving bandwidth and speeding up access. But if ETags are inconsistent across servers, clients might download content they already have, wasting bandwidth and slowing things down.

This inconsistency also means servers end up dealing with more requests for content that clients could have just used from their cache if ETags were consistent.

1. Etag - MDN ↩︎
1. If-Match - MDN ↩︎
1. If-None-Match - MDN ↩︎
1. GitHub CLI ↩︎
1. Weak validation ↩︎
1. Double quote in conditional header values ↩︎
1. Use weak comparison for Etags while caching ↩︎
## Recent posts

- Crossing the CORS crossroad
- Dysfunctional options pattern in Go
- Einstellung effect
- Strategy pattern in Go
- Anemic stack traces in Go
- Retry function in Go
- Type assertion vs type switches in Go
- Patching pydantic settings in pytest
- Omitting dev dependencies in Go binaries
- Eschewing black box API calls

