import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy import text

def main():
    engine = create_engine("mysql+mysqlconnector://root@35.194.162.35/wordpress")

    with engine.connect() as connection:
        result = connection.execute(text("select * from wp_comments"))
        for row in result:
            print("content:", row.comment_content)

if __name__ == '__main__':
    main()
