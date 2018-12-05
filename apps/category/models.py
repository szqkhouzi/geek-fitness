import mongoengine

class LoveFitness(mongoengine.Document):
    _id = mongoengine.StringField()
    b_cate = mongoengine.StringField()
    s_href = mongoengine.StringField()
    s_cate = mongoengine.StringField()
    title = mongoengine.StringField()
    img = mongoengine.StringField()
    date = mongoengine.StringField()
    datetime = mongoengine.StringField()
    category = mongoengine.StringField()
    href = mongoengine.StringField()
    author = mongoengine.StringField()
    content = mongoengine.StringField()
    content_img = mongoengine.StringField()
    video = mongoengine.StringField()
    content_html = mongoengine.StringField()

    def to_dict(self):
        dict = {
            '_id': self._id,
            'b_cate': self.b_cate,
            's_href': self.s_href,
            's_cate': self.s_cate,
            'title': self.title,
            'img': self.img,
            'date': self.date,
            'datetime': self.datetime,
            'catrgory': self.catrgory,
            'href': self.href,
            'author': self.author,
            'content': self.content,
            'content_img': self.content_img,
            'video': self.video,
            'content_html': self.content_html,
        }
        return dict

    class Meta:
        managed = False
        db_table = 'LoveFitness'

    meta = {'collection':'LoveFitness'}
