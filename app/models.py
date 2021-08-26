from app import db


class Domain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(64), index=True, unique=True)
    title = db.Column(db.String(200))
    available = db.Column(db.Boolean)
    ip = db.Column(db.String(50))
    check_date = db.Column(db.Date)
    check = db.Column(db.Boolean)
    check_title = db.relationship('InTitle', backref='url', lazy='dynamic')

    def __repr__(self):
        return '<Domain {}>'.format(self.url)


class UrlTag(db.Model):
    __tablename__ = 'urltag'
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(30), index=True, unique=True)

    def __repr__(self):
        return '<UrlTag {}>'.format(self.tag)


class TitleTag(db.Model):
    __tablename__ = 'titletag'
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(30), index=True, unique=True)
    def __repr__(self):
        return '<TitleTag {}>'.format(self.tag)


class TextTag(db.Model):
    __tablename__ = 'texttag'
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(30), index=True, unique=True)
    def __repr__(self):
        return '<TextTag {}>'.format(self.tag)


class CodePart(db.Model):
    __tablename__ = 'codepart'
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.Text, unique=True)

    def __repr__(self):
        return '<CodePart {}>'.format(self.tag)


class InTitle(db.Model):
    __tablename__ = 'intitle'
    __table_args__ = (
        db.PrimaryKeyConstraint('domain_id', 'tag_id'),
    )
    domain_id = db.Column(db.Integer, db.ForeignKey('domain.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('titletag.id'))


class InUrl(db.Model):
    __tablename__ = 'inurl'
    __table_args__ = (
        db.PrimaryKeyConstraint('domain_id', 'tag_id'),
    )
    domain_id = db.Column(db.Integer, db.ForeignKey('domain.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('urltag.id'))


class InText(db.Model):
    __tablename__ = 'intext'
    __table_args__ = (
        db.PrimaryKeyConstraint('domain_id', 'tag_id'),
    )
    domain_id = db.Column(db.Integer, db.ForeignKey('domain.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('texttag.id'))


class Double(db.Model):
    __tablename__ = 'double'
    __table_args__ = (
        db.PrimaryKeyConstraint('domain_id', 'tag_id'),
    )
    domain_id = db.Column(db.Integer, db.ForeignKey('domain.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('codepart.id'))
