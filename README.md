radio.api
=========

Internal abstraction API for the R/a/dio database.


Intent
======

The API intents to keep users from writing raw SQL (or other) queries for database access.
Instead an abstraction model based on data and intent is constructed that can be used.


Access
======

The API is constructed of several files and functions. All API access is done by calling functions.
A simple example would be to get the last played song as `radio.api.songs.last_played(n=1)`. Function
names are encouraged to be clear about their intent and return value.


Return values
=============

All API return values are of a python `dict` with a predefined format. This format should always be
explained at the top of the file. 

An example format for last played songs would be similar to this:
`{"played": "yesterday", "song": <song entry>, "player": "Wessie"}`

Failing to refer to a proper format spec is a bug and should be reported (and blamed).
