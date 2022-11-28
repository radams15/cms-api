# Database Documentation


The database is defined as the following:

```sqlite
CREATE TABLE "Article" (
    "id"	INTEGER NOT NULL UNIQUE,
    "title"	TEXT,
    "subtitle"	TEXT,
    "content"	TEXT NOT NULL,
    "header_img"	TEXT NOT NULL,
    "published"	INTEGER NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT)
);
```

Where:

- id is the article id
- title is the title of the article
- subtitle is the subtitle of the article
- content is the article body
- header_img is the URL to the image on the page header.
- published is the integer representation of the published date in epoch format.