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

d_of_i = "We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable rights, that among these are life, liberty and the pursuit of happiness. That to secure these rights, governments are instituted among men, deriving their just powers from the consent of the governed. That whenever any form of government becomes destructive to these ends, it is the right of the people to alter or to abolish it, and to institute new government, laying its foundation on such principles and organizing its powers in such form, as to them shall seem most likely to effect their safety and happiness. Prudence, indeed, will dictate that governments long established should not be changed for light and transient causes; and accordingly all experience hath shown that mankind are more disposed to suffer, while evils are sufferable, than to right themselves by abolishing the forms to which they are accustomed. But when a long train of abuses and usurpations, pursuing invariably the same object evinces a design to reduce them under absolute despotism, it is their right, it is their duty, to throw off such government, and to provide new guards for their future security."
process_target_string(d_of_i)


def test(s):
	for i in find_substring(s):
		print i

test('truth')

