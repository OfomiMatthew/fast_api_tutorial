from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL="sqlite:///./blog.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)