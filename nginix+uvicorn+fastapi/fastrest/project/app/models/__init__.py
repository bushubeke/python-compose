#pip install SQLAlchemy==1.4.3 aiosqlite
import aiosqlite
from sqlalchemy import create_engine
from sqlalchemy.dialects.sqlite import pysqlite
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///../fastauth.db"

engine = create_async_engine(DATABASE_URL, future=True, echo=True)
syncengine=create_engine('sqlite:///../fastauth.db', \
                       convert_unicode=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()   


#Base.metadata.create_all(bind=syncengine)
#Base.metadata.drop_all(bind=syncengine)

    