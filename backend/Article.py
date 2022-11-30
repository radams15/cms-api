from datetime import datetime


class Article:

    def __init__(self, title: str, subtitle: str, content: str, header_img: str, published, id: int = None):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.content = content
        self.header_img = header_img

        if isinstance(published, datetime):
            self.published = published
        else:
            self.published = datetime.fromtimestamp(int(published))

    @staticmethod
    def from_json(json: dict):
        return Article(
            json.get('title'),
            json.get('subtitle'),
            json.get('content'),
            json.get('header_img'),
            json.get('published'),
            json['id'] if 'id' in json.keys() else None
        )

    def to_json(self):
        out = {
            'title': self.title,
            'subtitle': self.subtitle,
            'content': self.content,
            'header_img': self.header_img,
            'published': int(self.published.timestamp())
        }

        if self.id:
            out['id'] = self.id

        return out

    def __repr__(self):
        return f'Article({self.title})'
