# API Documentation

## `GET /api/v1/article/`

Returns JSON representation of all articles.

Return data:

```json
{
    "title": "gdlgds",
    "subtitle" : "jiryjf",
    "content" : "hlkjhkhdf",
    "headerImg" : "https://gsgsddgs",
    "published": 1669633879
}
```

Where:

- title: str required
- subtitle: str
- content: str
- headerImg: str
- published: int (epoch time representation of date & time)

## `GET /api/v1/article/<id>`

Returns JSON representation of an article.

`id` = integer id of article to get

Return data:

```json
{
    "title": "gdlgds",
    "subtitle" : "jiryjf",
    "content" : "hlkjhkhdf",
    "headerImg" : "https://gsgsddgs",
    "published": 1669633879
}
```

Where:

- title: str required
- subtitle: str
- content: str
- headerImg: str
- published: int (epoch time representation of date & time)

## `POST /api/v1/article`

Creates a new article on the site.

Post data: 

```json
{
    "title": "gdlgds",
    "subtitle" : "jiryjf",
    "content" : "hlkjhkhdf",
    "headerImg" : "https://gsgsddgs",
    "published": 1669633879
}
```

This then returns the status (201 success or otherwise failure), and the id of the added article. 

Returned data:

```json
{
  "status": 201,
  "id": 1
}
```

## `PUT /api/v1/article`

Creates a new article on the site.

Post data: 

```json
{
    "title": "gdlgds",
    "subtitle" : "jiryjf",
    "content" : "hlkjhkhdf",
    "headerImg" : "https://gsgsddgs",
    "published": 1669633879,
    "id": 4
}
```

This then returns the status (201 success or otherwise failure), and the id of the updated article. 

Returned data:

```json
{
  "status": 201,
  "id": 1
}
```