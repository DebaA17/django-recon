
from django.shortcuts import render

import dns.resolver
import socket
import requests
import whois


def home(request):
	domain = request.GET.get('domain')
	dns_records = []
	whois_info = 'N/A'
	security_headers = []
	ip_geo = 'N/A'
	asn = 'N/A'
	isp = 'N/A'
	security_checks = [
		{'name': 'SPF', 'valid': False},
		{'name': 'DMARC', 'valid': False},
		{'name': 'DKIM', 'valid': False},
		{'name': 'DNSSEC', 'valid': False},
		{'name': 'CAA', 'valid': False},
	]
	if domain:
		record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA', 'CNAME', 'CAA']
		resolver = dns.resolver.Resolver()
		resolver.nameservers = ['8.8.8.8', '1.1.1.1']
		for rtype in record_types:
			try:
				answers = resolver.resolve(domain, rtype, lifetime=3)
				for r in answers:
					value = str(r.to_text())
					dns_records.append({'type': rtype, 'value': value})
			except Exception:
				pass
		# Security checks
		security_checks = [
			{'name': 'SPF', 'valid': any(r['type'] == 'TXT' and 'v=spf1' in r['value'] for r in dns_records)},
			{'name': 'DMARC', 'valid': any(r['type'] == 'TXT' and 'v=DMARC1' in r['value'] for r in dns_records)},
			{'name': 'DKIM', 'valid': any(r['type'] == 'TXT' and 'dkim' in r['value'].lower() for r in dns_records)},
			{'name': 'DNSSEC', 'valid': False},  # DNSSEC check needs more logic
			{'name': 'CAA', 'valid': any(r['type'] == 'CAA' for r in dns_records)},
		]
		# Security score calculation
		score = 0
		for check in security_checks:
			if check['valid']:
				score += 20
		# WHOIS info
		try:
			w = whois.whois(domain)
			whois_info = w.text if w.text else str(w)
		except Exception:
			whois_info = 'WHOIS lookup failed.'
		# Security headers check
		try:
			resp = requests.get(f'http://{domain}', timeout=5)
			headers = resp.headers
			header_checks = [
				('Strict-Transport-Security', 'Strict-Transport-Security' in headers),
				('Content-Security-Policy', 'Content-Security-Policy' in headers),
				('X-Frame-Options', 'X-Frame-Options' in headers),
				('X-Content-Type-Options', 'X-Content-Type-Options' in headers),
				('Referrer-Policy', 'Referrer-Policy' in headers),
				('Permissions-Policy', 'Permissions-Policy' in headers),
				('X-XSS-Protection', 'X-XSS-Protection' in headers),
			]
			security_headers = [{'name': h[0], 'present': h[1]} for h in header_checks]
		except Exception:
			security_headers = [{'name': 'Header check failed', 'present': False}]
		# IP/ASN/ISP info
		try:
			ip = socket.gethostbyname(domain)
			ipinfo = requests.get(f'https://ipinfo.io/{ip}/json', timeout=3).json()
			ip_geo = ipinfo.get('city', '') + ', ' + ipinfo.get('region', '') + ', ' + ipinfo.get('country', '')
			asn = ipinfo.get('org', 'N/A')
			isp = ipinfo.get('org', 'N/A')
		except Exception:
			ip_geo = 'Lookup failed.'
			asn = 'N/A'
			isp = 'N/A'
	else:
		score = 0
	# Client info
	client_ip = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
	if client_ip in ['127.0.0.1', '::1', 'localhost']:
		# Get public IP from external service
		try:
			client_ip = requests.get('https://api.ipify.org').text
		except Exception:
			client_ip = 'Unknown'
	client_ua = request.META.get('HTTP_USER_AGENT', 'Unknown')
	client_isp = 'N/A'
	client_location = 'N/A'
	try:
		cipinfo = requests.get(f'https://ipinfo.io/{client_ip}/json', timeout=3).json()
		client_isp = cipinfo.get('org', 'N/A')
		client_location = cipinfo.get('city', '') + ', ' + cipinfo.get('region', '') + ', ' + cipinfo.get('country', '')
	except Exception:
		pass
	context = {
		'dns_records': dns_records,
		'security_checks': security_checks,
		'security_score': score,
		'whois_info': whois_info,
		'ip_geo': ip_geo,
		'asn': asn,
		'isp': isp,
		'domain': domain or '',
		'client_ip': client_ip,
		'client_ua': client_ua,
		'client_isp': client_isp,
		'client_location': client_location,
		'security_headers': security_headers,
	}
	return render(request, 'home.html', context)
