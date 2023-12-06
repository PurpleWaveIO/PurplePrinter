from flask import Flask, render_template, request
import ldap

app = Flask(__name__,template_folder='templates')

# LDAP configuration
LDAP_SERVER = 'ldap://{ip_address}'
LDAP_PORT = 389
LDAP_DOMAIN = 'example.com'
LDAP_SEARCH_BASE = 'ou=users,dc=example,dc=com'

@app.route('/', methods=['GET', 'POST'])

def ldap_lookup():
    if request.method == 'POST':
        ip_address = request.form.get('ip_address')
        username = request.form.get('username')
        password = request.form.get('password')

        # Construct the LDAP URL
        ldap_url = f"{LDAP_SERVER}:{LDAP_PORT}"
        ldap_conn = ldap.initialize(ldap_url)
        ldap_conn.protocol_version = 3

        # Bind to the LDAP server
        ldap_conn.simple_bind_s(f"{username}@{LDAP_DOMAIN}", password)

        # Perform the LDAP search
        search_filter = f"(host={ip_address})"
        result = ldap_conn.search_s(LDAP_SEARCH_BASE, ldap.SCOPE_SUBTREE, search_filter)

        # Extract the LDAP attributes you need
        ldap_attributes = [entry[1] for entry in result]

        return render_template('result.html', ldap_attributes=ldap_attributes)

    return render_template('status.html')

@app.route('/config')
def config_page():
    return render_template('config.html')

@app.route('/status')
def status_page():
    return render_template('status.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
