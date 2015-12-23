# Creating Flasky - the simple blogging site

## Folders

Create the following folders inside your main app folder.
Make sure the names are spelled correctly.

`__ /flasky
	 |__ /static
	 |__ /templates`

`/flasky`			is the app folder (you can chose any name you like)
`/flasky/static`	is the folder that contains js, css, img files used by the app
`/flasky/templates`	is the folder that contains the views (html file templates) of your app

## Using sqlite3

The following is the schema of the SQL database.

```sql
drop table if exists list;

create table list (
	id integer primary key autoincrement,
	title text not null,
	'text' text not null
)
```

## Configuration file

Our app will take the configuration from a separate file.
So let's create that: `flasky.cfg` - check the contents [here](flasky.cfg)

