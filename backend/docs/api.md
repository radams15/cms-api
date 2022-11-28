# API Documentation

## `GET /article/<id>`

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

## `POST /article`

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