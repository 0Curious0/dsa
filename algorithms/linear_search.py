def linear_search(lst, item):
	for i in lst:
		if i == item:
			return lst.index(i)

	return None
