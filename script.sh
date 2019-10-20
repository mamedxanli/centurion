docker cp dbbackup_script.sh centurion_db_1:/tmp
docker exec -u postgres centurion_db_1 ./tmp/dbbackup_script.sh
docker cp centurion_db_1:/tmp/db_backup db_backup/db_backup

