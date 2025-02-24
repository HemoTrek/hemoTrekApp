@echo off

:: initDB.bat - A script to build a local SQLite database from schema.sql
:: Make sure sqlite3.exe is installed or on your PATH

echo Creating local SQLite database...
sqlite3 patients.db < schema.sql

echo Done! The database has been built as patients.db
pause
