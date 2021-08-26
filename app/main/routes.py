from app import app, db
from app.main import bp
from app.main.forms import UploadDomainList
from app.models import Domain
from flask import render_template, request, flash


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    form = UploadDomainList()
    if form.validate_on_submit():
        print("VALIDATE")
        if request.method == 'POST':
            upload_file = request.files['upload_filename']
            if upload_file and \
                    ('.' in upload_file.filename) and \
                    (upload_file.filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']):
                flash('Файл загружен')
                afile = request.files['upload_filename'].read().decode('utf-8')
                lines = [x.strip() for x in afile.split('\n')]
                for item in lines:
                    item = item.lower()
                    if Domain.query.filter(Domain.url==item).first():
                        continue
                    domain = Domain(url=item, check=False)
                    try:
                        db.session.add(domain)
                        db.session.commit()
                    except Exception as e:
                        print("ERROR" , str(e))
    return render_template('main/index.html', form=form, title="Главная")


@bp.route('/tags')
def tags():
    return render_template('main/tags.html', title="Тэги")
