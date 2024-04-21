MYSQL_CONFIG = {
    'host': '1.251.203.204:33065',
    'user': 'root',
    'password': 'kdt5',
    'database': 'Team5'
}

DB_MYSQL_URL = 'mysql+pymysql://{user}:{password}@{host}/{database}'.format(
    **MYSQL_CONFIG
)

SQLALCHEMY_DATABASE_URI = DB_MYSQL_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False