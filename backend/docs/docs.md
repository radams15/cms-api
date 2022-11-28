# Backend Documentation

## `GET /article/<id>`

Returns JSON representation of an article.

`id` = integer id of article to get

Return data:

```json
{
    "title": "gdlgds",
    "subHeading" : "jiryjf",
    "content" : "hlkjhkhdf",
    "headerImage" : "https://gsgsddgs",
    "datePublishged": "30/12/2010"
}
```

## `POST /article`

Creates a new article on the site.

Post data: 

```json
{
    "title": "gdlgds",
    "subHeading" : "jiryjf",
    "content" : "hlkjhkhdf",
    "headerImage" : "https://gsgsddgs",
    "datePublishged": "30/12/2010"
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