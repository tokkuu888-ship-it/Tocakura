import os
import subprocess
import sys

print("Starting backend deployment...")
print(f"Current directory: {os.getcwd()}")
print(f"PORT environment variable: {os.environ.get('PORT', '8000')}")

try:
    os.chdir('backend')
    print(f"Changed to directory: {os.getcwd()}")
    print("Starting uvicorn...")
    result = subprocess.run([sys.executable, '-m', 'uvicorn', 'app.main:app', '--host', '0.0.0.0', '--port', os.environ.get('PORT', '8000')], check=True)
    print(f"Uvicorn exited with code: {result.returncode}")
except Exception as e:
    print(f"Error starting backend: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
