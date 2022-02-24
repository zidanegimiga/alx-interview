# Log Parsing

Script that reads stdin line by line and computes required metrics.
Input format:
      '<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>'
Required metrics:
- File size: total size
- Number of lines by status code:
  - Possible status codes: [200, 301, 400,401, 403, 404, 405, 500]
  - status codes printed in ascending order

These metrics are printed after every 10 lines and/or on a keyboard interruption (CTRL + C)
