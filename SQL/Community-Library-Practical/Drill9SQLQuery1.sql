SELECT BC.No_Of_Copies, BK.Title, LB.BranchName
From BOOK_COPIES AS BC
INNER JOIN LIBRARY_BRANCH AS LB
ON BC.BranchId = LB.BranchId
INNER JOIN BOOK AS BK 
ON BK.BookId = BC.BookID
WHERE LB.BranchName = 'Sharpstown' AND BK.Title = 'The Lost Tribe'