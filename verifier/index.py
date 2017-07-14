import puzzle


def checkSudoku(rows):

  def isValidSet(s):
      s = sorted(s)
      for i in range (0, len(s)):
        if s[i] != i+1:
          return False

      return True

  for i in range(0, 9):
    row = rows[i]
    column = []
    section = []

    for j in range(0, 9):
      rowMarker = ((i / 3) * 3) + j / 3
      columnMarker = (i * 3) % 9 + j % 3

      column.append(row[j])
      section.append(rows[rowMarker][columnMarker])


    if not isValidSet(column) or not isValidSet(row) or not isValidSet(section):
      return False

  return True


print checkSudoku(puzzle.solved)
