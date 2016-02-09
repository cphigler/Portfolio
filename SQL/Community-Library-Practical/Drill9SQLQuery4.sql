SELECT B.Title, BR.Name, BR.[Address], LB.BranchName, BL.DueDate
FROM BOOK_LOANS AS BL
INNER JOIN BORROWER AS BR
ON BL.CardNo = BR.CardNo
INNER JOIN LIBRARY_BRANCH AS LB 
ON BL.BranchId = LB.BranchId
INNER JOIN BOOK AS B
ON B.BookId =BL.BookId
WHERE LB.BranchName = 'Sharpstown' AND BL.DueDate = '5/29/2015'
