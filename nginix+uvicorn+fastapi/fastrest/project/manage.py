from app import create_dev_app,create_prod_app


import os

import uvicorn


# basde=os.path.abspath(os.path.dirname(__file__))

# MIGRATION_DIR = os.path.join(basde, 'devmigrations')

    

app=create_dev_app()


if __name__=="__main__":
    uvicorn.run(app, port=9000, host='0.0.0.0')
