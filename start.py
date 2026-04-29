import os
import subprocess
import sys

os.chdir('backend')
subprocess.run([sys.executable, '-m', 'uvicorn', 'app.main:app', '--host', '0.0.0.0', '--port', os.environ.get('PORT', '8000')])
