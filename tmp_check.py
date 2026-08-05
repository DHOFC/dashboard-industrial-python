import sys
import importlib.metadata as m
print('python', sys.executable)
print('streamlit', m.version('streamlit'))
print('starlette', m.version('starlette'))
print('uvicorn', m.version('uvicorn'))
