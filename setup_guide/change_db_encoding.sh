#!/usr/bin/env bash
# Change database encoding to utf-8

mysqldump --user=root --password=ainaa --default-character-set=latin1 --skip-set-charset posov5 > dump.sql
sed -r 's/latin1/utf8/g' dump.sql > dump_utf.sql
mysql --user=root --password=ainaa --execute="DROP DATABASE posov5; CREATE DATABASE posov5 CHARACTER SET utf8 COLLATE utf8_general_ci;"
mysql --user=root --password=ainaa --default-character-set=utf8 posov5 < dump_utf.sql
