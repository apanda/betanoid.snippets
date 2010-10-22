#!/usr/bin/env python
from flask import Flask
from flask import request
import logging
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'HEAD', 'DELETE', 'PUT', 'OPTIONS'])
def test():
    xmlResp = """
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>PayloadContent</key>
	<array>
		<dict>
			<key>FullScreen</key>
			<false/>
			<key>IsRemovable</key>
			<true/>
			<key>Label</key>
			<string>Google</string>
			<key>PayloadDescription</key>
			<string>Configures Web Clip</string>
			<key>PayloadDisplayName</key>
			<string>Web Clip (Google)</string>
			<key>PayloadIdentifier</key>
			<string>com.betanoid.text.WebClip</string>
			<key>PayloadOrganization</key>
			<string>Betanoid</string>
			<key>PayloadType</key>
			<string>com.apple.webClip.managed</string>
			<key>PayloadUUID</key>
			<string>0621C761-15E4-45A5-9E20-F5A9B3D276BB</string>
			<key>PayloadVersion</key>
			<integer>1</integer>
			<key>Precomposed</key>
			<false/>
			<key>URL</key>
			<string>http://google.com</string>
		</dict>
	</array>
	<key>PayloadDescription</key>
	<string>Betanoid</string>
	<key>PayloadDisplayName</key>
	<string>Betanoid Test</string>
	<key>PayloadIdentifier</key>
	<string>com.betanoid.text</string>
	<key>PayloadOrganization</key>
	<string>Betanoid</string>
	<key>PayloadRemovalDisallowed</key>
	<false/>
	<key>PayloadType</key>
	<string>Configuration</string>
	<key>PayloadUUID</key>
	<string>F2FF39A8-8F45-4D29-8757-CC9BD82AF6E0</string>
	<key>PayloadVersion</key>
	<integer>1</integer>
</dict>
</plist>
    """
    app.logger.debug(request.method + " " + request.data)

    return xmlResp

if __name__ == "__main__":
    logging.basicConfig(filename='test.log')
    app.run(host='0.0.0.0', debug=True)
