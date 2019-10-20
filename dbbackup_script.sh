#!/bin/sh

#su - postgres
pg_dump postgres -f /tmp/db_backup
