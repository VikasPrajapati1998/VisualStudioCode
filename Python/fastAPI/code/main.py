'''
Operation in HTTP request methods:
    1. POST     # @app.post()
    2. GET      # @app.get()
    3. PUT      # @app.put()
    4. DELETE   # @app.delete()
    5. OPTIONS  # @app.options()
    6. HEAD     # @app.head()
    7. PATCH    # @app.patch()
    8. TRACE    # @app.trace()
'''

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Hello World"}

