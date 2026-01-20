# HTTP ETag Caching

Source: https://rednafi.com/misc/etag_and_http_caching/

## Overview

The HTTP `ETag` header enables client-side caching for GET requests. Works with conditional headers `If-Match` and `If-None-Match`.

## Basic Workflow

1. Client makes GET request
2. Server responds with 200 OK + `ETag` header
3. Client caches response and ETag value
4. Subsequent requests include `If-None-Match` header with cached ETag
5. Server compares ETags:
   - Match → 304 Not Modified (no body, use cache)
   - No match → 200 OK + new content + new ETag

```
Client                                 Server
  |                                       |
  |----- GET Request -------------------->|
  |<---- Response 200 OK + ETag ----------|
  |     (Cache response locally)          |
  |                                       |
  |----- GET Request + If-None-Match ---->|
  |       Does ETag match?                |
  |<---- Yes: 304 Not Modified -----------|  (Use local cache)
  |       No: 200 OK + New ETag ----------|  (Update cache)
```

## Key Points

- **Weak ETags** (`W/"..."` prefix): Don't compare bit-by-bit. Two JSON payloads with same content but different formatting are semantically equal
- **Always quote ETags** in `If-None-Match` header per spec
- **Weak comparison** for `If-None-Match`: Client can validate cache even with slight representation changes
- **Browsers auto-manage**: Send conditional requests automatically

## Example: GitHub API

```bash
# Initial request
gh api -i /users/rednafi
# Returns: Etag: W/"b8fdfabd59aed6e0e602dd140c0a0ff48a665cac791dede458c5109bf4bf9463"

# Subsequent request with If-None-Match
gh api -i -H 'If-None-Match: W/"b8fdfabd..."' /users/rednafi
# Returns: HTTP/2.0 304 Not Modified
```

## Go Server Implementation

```go
func calculateETag(content string) string {
    hasher := sha256.New()
    hasher.Write([]byte(content))
    hash := hex.EncodeToString(hasher.Sum(nil))
    return fmt.Sprintf("W/\"%s\"", hash)
}

http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
    content := `{"message": "Hello, world!"}`
    eTag := calculateETag(content)

    ifNoneMatch := strings.TrimPrefix(
        strings.Trim(r.Header.Get("If-None-Match"), "\""), "W/")
    contentHash := strings.TrimPrefix(eTag, "W/")

    if ifNoneMatch == strings.Trim(contentHash, "\"") {
        w.WriteHeader(http.StatusNotModified)
        return
    }

    w.Header().Set("ETag", eTag)
    w.Header().Set("Content-Type", "application/json")
    w.WriteHeader(http.StatusOK)
    fmt.Fprint(w, content)
})
```

## Multi-Server Consistency

**Critical**: All servers behind a load balancer must generate identical ETags for identical content. Inconsistent ETags cause:
- Unnecessary downloads of cached content
- Wasted bandwidth
- Increased server load

For static content, configure at load balancer level. For dynamic content, implement in middleware.
