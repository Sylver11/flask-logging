from flask import current_app, _app_ctx_stack
import logging
import logging.config
from logging.handlers import SMTPHandler


class LOG(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        logging.config.fileConfig('logging_config.ini', disable_existing_loggers=False)
        return logging.getLogger(__name__)
        #app.teardown_appcontext(self.teardown)

#    def connect(self):
#        return sqlite3.connect(current_app.config['SQLITE3_DATABASE'])
#
#    def teardown(self, exception):
#        ctx = _app_ctx_stack.top
#        if hasattr(ctx, 'sqlite3_db'):
#            ctx.sqlite3_db.close()

    def add_mail_handler(testing=False):
        mail_handler = SMTPHandler(
                mailhost='127.0.0.1',
                fromaddr='server-error@example.com',
                toaddrs=['admin@example.com'],
                subject='Application Error'
            )
        mail_handler.setLevel(logging.ERROR)
        mail_handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s'))

    if not current_app.debug or testing:
        current_app.logger.addHandler(mail_handler)
