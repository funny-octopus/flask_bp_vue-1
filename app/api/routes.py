import json
from app.api import bp
from app import db
from app.models import UrlTag, TextTag, TitleTag, CodePart
from flask import jsonify, request, make_response


@bp.route('/tags', methods=['GET', 'POST', 'PUT', 'DELETE'])
def tags():
    if request.method == 'GET':
        url_tags = UrlTag.query.all()
        url_tags = [item.tag for item in url_tags]
        text_tags = TextTag.query.all()
        text_tags = [item.tag for item in text_tags]
        title_tags = TitleTag.query.all()
        title_tags = [item.tag for item in title_tags]
        code_part = CodePart.query.all()
        code_part = [item.tag for item in code_part]
        res_dict = {'url_tags': url_tags,
                    'text_tags': text_tags,
                    'title_tags': title_tags,
                    'code_part': code_part}
        response = make_response(jsonify(res_dict))
        response.headers['Content-Type'] = 'application/json'
        return response
    if request.method == 'POST':
        r = request.get_data().decode()
        r_json = json.loads(r)
        print(r_json['text_tags'])
        response = make_response({'status': 'ok',})
        return response
