import requests

import base64


def get_vt_report(url, api_key):
    if not api_key:
        return None

    headers = {"x-apikey": api_key}
    url_id = base64.urlsafe_b64encode(url.encode()).decode().strip('=')
    analysis_url = f"https://www.virustotal.com/api/v3/urls/{url_id}"

    response = requests.get(analysis_url, headers=headers)
    if response.status_code == 200:
        data = response.json()['data']['attributes']
        stats = data['last_analysis_stats']
        vendor_results = data['last_analysis_results']

        return {
            'url': url,
            'malicious': stats['malicious'],
            'harmless': stats['harmless'],
            'suspicious': stats['suspicious'],
            'undetected': stats['undetected'],
            'total_checks': sum(stats.values()),
            'vendor_results': vendor_results,
            'last_analysis_date': data['last_analysis_date'],
            'vt_link': f"https://www.virustotal.com/gui/url/{url_id}/detection"
        }
    return None
