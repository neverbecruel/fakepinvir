from Fakinterest import app
from Fakinterest import database, app
from Fakinterest.models import Usuarios, Foto
import logging
from time import sleep


with app.app_context():
    database.create_all()

if __name__ == '__main__':
    app.run(debug=True)

logger = logging.getLogger(__name__)
while True:
    logging.debug('Keeping server running...')
    sleep(10)




