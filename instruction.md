A web-server access log in Apache "combined" format is at /app/access.log. Parse it and write a JSON summary to the absolute path /app/report.json.

/app/report.json must be a single JSON object with exactly these three keys:

- "total_requests" (integer): the number of non-empty request lines in the log.
- "unique_ips" (integer): the number of distinct client IP addresses. The client IP is the first whitespace-separated field of each line.
- "top_path" (string): the request path that appears most often. The path is the second token inside the quoted request line, e.g. "/index.html" in `"GET /index.html HTTP/1.1"`.

Success criteria:

1. /app/report.json exists and contains a single valid JSON object.
2. "total_requests" equals the number of non-empty request lines in /app/access.log.
3. "unique_ips" equals the number of distinct client IP addresses in /app/access.log.
4. "top_path" equals the most frequently requested path in /app/access.log.
