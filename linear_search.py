# linear search algorithm
# the complexity is O(n)
def linear_search(l, v):
  for item in l:
    if item == v:
      return True
  return False
print(linear_search([1,2,3,4,5], 3))
