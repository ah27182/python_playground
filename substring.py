chr_indices = {}

def process_target_string(string):
	for i, c in enumerate(string):
		if c not in chr_indices:
			chr_indices[c] = set()

		chr_indices[c].add(i)


def find_substring(substring):
	if not substring:
		return

	check = True

	for i in chr_indices[substring[0]]:
		# print i
		rest = enumerate(substring)
		rest.next()

		for offset, c in rest:
			check = check and ((i + offset) in chr_indices[c])
			if not check:
				break

		if check:
			yield i

		check = True

def test(s):
	for i in find_substring(s):
		print i

test('truth')

