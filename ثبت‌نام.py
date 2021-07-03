def check_registration_rules(**kw):
	lst = []
	for username, password in kw.items():
		if len(username) >= 4 and username != 'codecup' and username != 'quera' and len(password) >= 6:
			is_digits = 0
			if password.isdigit():
				is_digits = 1
			if not is_digits:
				lst.append(username)

	return lst
