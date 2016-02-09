SELECT BR.Name, BR.[Address], COUNT(BL.CardNo) AS 'No of Books Checked Out'
FROM BOOK_LOANS AS BL
INNER JOIN BORROWER AS BR
ON BL.CardNo = BR.CardNo
GROUP BY BR.Name, BR.[Address] 
HAVING COUNT(BL.CardNo) > 5

