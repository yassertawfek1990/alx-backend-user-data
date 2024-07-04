#!/usr/bin/env python3
"""A module for filtering log entries."""
import os
import re
import logging
import mysql.connector
from typing import List


regex_patterns = {
    'pattern_builder': lambda fields, sep: r'(?P<field>{})=[^{}]*'
    .format('|'.join(fields), sep),
    'replacement': lambda repl: r'\g<field>={}'.format(repl),
}
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str,
        ) -> str:
    """Anonymizes specific fields in a log line."""
    pattern, substitute = (regex_patterns["pattern_builder"],
                           regex_patterns["replacement"])
    return re.sub(pattern(fields, separator), substitute(redaction), message)


def get_logger() -> logging.Logger:
    """Sets up a logger for sensitive user information."""
    user_logger = logging.getLogger("user_activity")
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    user_logger.setLevel(logging.INFO)
    user_logger.propagate = False
    user_logger.addHandler(handler)
    return user_logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Establishes a connection to the database."""
    db_host = os.getenv("DB_HOST", "localhost")
    db_name = os.getenv("DB_NAME", "")
    db_user = os.getenv("DB_USER", "root")
    db_pwd = os.getenv("DB_PASSWORD", "")
    connection = mysql.connector.connect(
        host=db_host,
        port=3306,
        user=db_user,
        password=db_pwd,
        database=db_name,
    )
    return connection


def main():
    """Logs user data from the database."""
    columns = "name,email,phone,ssn,password,ip,last_login,user_agent"
    column_list = columns.split(',')
    sql_query = "SELECT {} FROM users;".format(columns)
    logger = get_logger()
    db_connection = get_db()
    with db_connection.cursor() as cursor:
        cursor.execute(sql_query)
        records = cursor.fetchall()
        for record in records:
            log_entry = map(
                lambda x: '{}={}'.format(x[0], x[1]),
                zip(column_list, record),
            )
            log_message = '{};'.format('; '.join(list(log_entry)))
            log_args = ("user_activity", logging.INFO,
                        None, None, log_message, None, None)
            log_record = logging.LogRecord(*log_args)
            logger.handle(log_record)


class RedactingFormatter(logging.Formatter):
    """Formatter class that obfuscates sensitive information."""

    MASK = "***"
    LOG_FORMAT = "[COMPANY] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    FORMAT_FIELDS = ('name', 'levelname', 'asctime', 'message')
    DELIMITER = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.LOG_FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formats a log record by obfuscating sensitive information.
        """
        log_message = super(RedactingFormatter, self).format(record)
        obfuscated_message = filter_datum(self.fields, self.MASK,
                                          log_message, self.DELIMITER)
        return obfuscated_message


if __name__ == "__main__":
    main()
