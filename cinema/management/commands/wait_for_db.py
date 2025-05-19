import time
import MySQLdb
import os
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for MySQL database...")
        db_ready = False
        while not db_ready:
            try:
                conn = MySQLdb.connect(
                    host=os.environ.get('DB_HOST', 'db'),
                    user=os.environ.get('DB_USER', 'cinema_user'),
                    passwd=os.environ.get('DB_PASSWORD', 'cinema_pass'),
                    db=os.environ.get('DB_NAME', 'cinema_db')
                )
                conn.close()
                db_ready = True
            except MySQLdb.OperationalError:
                self.stdout.write("MySQL not available, waiting...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("MySQL is ready!"))
