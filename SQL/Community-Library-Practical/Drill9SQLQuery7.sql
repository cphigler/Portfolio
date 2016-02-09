SELECT BK.Title, BA.AuthorName, LB.BranchName, BC.No_Of_Copies
FROM BOOK AS BK
INNER JOIN BOOK_AUTHORS AS BA
ON BK.BookId = BA.BookId
INNER JOIN BOOK_COPIES AS BC
ON BK.BookId = BC.BookId
INNER JOIN LIBRARY_BRANCH AS LB 
ON LB.BranchId = BC.BranchId
WHERE BA.AuthorName = 'Stephen King' AND LB.BranchName = 'Central'
