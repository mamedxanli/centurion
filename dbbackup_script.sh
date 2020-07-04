#!/bin/sh

#su - postgres
pg_dump postgres -U postgres -f /tmp/db_backup
