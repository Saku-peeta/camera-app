import os
import http.server
import socketserver
import sys

PORT = 8000
DIRECTORY = "public"

# Python 3.7以上かどうかチェック
python_version = sys.version_info
if python_version.major == 3 and python_version.minor >= 7:
    # Python 3.7以上の場合は、directoryパラメータを使用
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=DIRECTORY, **kwargs)

        def do_GET(self):
            if self.path == '/':
                self.path = '/camera.html'
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
else:
    # Python 3.7未満の場合は、ディレクトリを変更してからハンドラーを使用
    os.chdir(DIRECTORY)
    class Handler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/':
                self.path = '/camera.html'
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

if not os.path.exists(DIRECTORY):
    os.makedirs(DIRECTORY)

print(f"サーバーが起動しました: http://localhost:{PORT}")
print("終了するには Ctrl+C を押してください")

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\nサーバーを停止しています...")
except Exception as e:
    print(f"エラーが発生しました: {e}") 