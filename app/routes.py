from flask import render_template, request, redirect, jsonify, current_app
from . import app, db
from .models import URL
from .utils import get_vt_report
import string, random, validators


def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


@app.route('/', methods=['GET', 'POST'])
def index():
    vt_result = None
    short_url = None
    error = None

    if request.method == 'POST':
        original_url = request.form['url']

        if not validators.url(original_url):
            error = "Invalid URL!"
        else:
            vt_result = get_vt_report(original_url, current_app.config['VT_API_KEY'])

            if vt_result and vt_result['malicious'] > 0:
                error = "⚠️ Malicious URL detected!"
            else:
                existing_url = URL.query.filter_by(original_url=original_url).first()
                if existing_url:
                    short_url = request.host_url + existing_url.short_url
                else:
                    short_key = generate_short_url()
                    new_url = URL(original_url=original_url, short_url=short_key)
                    db.session.add(new_url)
                    db.session.commit()
                    short_url = request.host_url + short_key

    return render_template('index.html', short_url=short_url, vt_result=vt_result, error=error)


@app.route('/<short_url>')
def redirect_url(short_url):
    url = URL.query.filter_by(short_url=short_url).first_or_404()
    return redirect(url.original_url)


@app.route('/api/shorten', methods=['POST'])
def api_shorten():
    data = request.get_json()
    original_url = data.get('url')

    if not validators.url(original_url):
        return jsonify({'error': 'Invalid URL'}), 400

    if get_vt_report(original_url, current_app.config['VT_API_KEY']):
        return jsonify({'error': 'URL detected as malicious', 'malicious': True}), 400

    existing_url = URL.query.filter_by(original_url=original_url).first()
    if existing_url:
        short_url = existing_url.short_url
    else:
        short_url = generate_short_url()
        new_url = URL(original_url=original_url, short_url=short_url)
        db.session.add(new_url)
        db.session.commit()

    return jsonify({'short_url': request.host_url + short_url, 'malicious': False})
