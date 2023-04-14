# Verify MySQLdb package installation
try:
    import MySQLdb
    print('MySQLdb package is installed properly.')
except ImportError:
    print('MySQLdb package is not installed.')
