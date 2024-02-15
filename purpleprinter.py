from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import ldap

app = Flask(__name__)

# LDAP configuration
LDAP_PORT = 389
LDAP_DOMAIN = 'local.domain'  # e.g. 'example.com'
LDAP_SEARCH_BASE = 'ou=users,dc=local,dc=domain'

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('status_page'))
    return render_template('login.html', error=error)

#Route for handling LDAP request
@app.route('/', methods=['GET', 'POST'])
def ldap_lookup():
    if request.method == 'POST':
        ip_address = request.form.get('ip_address')

        # Construct the LDAP URL with user-supplied IP address
        ldap_server = f"ldap://{ip_address}"
        ldap_url = f"{ldap_server}:{LDAP_PORT}"
        ldap_conn = ldap.initialize(ldap_url)
        ldap_conn.protocol_version = 3

        # Bind to the LDAP server. Change User and Password here that you want to capture
        ldap_conn.simple_bind_s('USERNAME', 'PASSWORD')

        # Perform the LDAP search
        search_filter = f"(host={ip_address})"
        result = ldap_conn.search_s(LDAP_SEARCH_BASE, ldap.SCOPE_SUBTREE, search_filter)

        # Extract the LDAP attributes you need
        ldap_attributes = [entry[1] for entry in result]

        return render_template('result.html', ldap_attributes=ldap_attributes)

    return render_template('config.html')

#Route for Config page
@app.route('/config')
def config_page():
    return render_template('config.html')

#Route for Status page
@app.route('/status')
def status_page():
    return render_template('status.html')

#Route for Paper / Tray page
@app.route('/tray')
def tray_page():
    return render_template('tray.html')

#Enable built in web server and debug
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
