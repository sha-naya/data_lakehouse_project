CREATE TABLE Persons (
    TransactionID int,
    TransactionTime datetime,
    TransactionCost numeric,
);

GO

INSERT INTO Persons (TransactionID, TransactionTime, TransactionCost)
VALUES (1, GETDATE()-5, 15.50);
INSERT INTO Persons (TransactionID, TransactionTime, TransactionCost)
VALUES (2, GETDATE()-4, 17.00);
INSERT INTO Persons (TransactionID, TransactionTime, TransactionCost)
VALUES (3, GETDATE()-3, 15.50);
INSERT INTO Persons (TransactionID, TransactionTime, TransactionCost)
VALUES (4, GETDATE()-2, 17.00);
INSERT INTO Persons (TransactionID, TransactionTime, TransactionCost)
VALUES (5, GETDATE()-1, 17.00);
INSERT INTO Persons (TransactionID, TransactionTime, TransactionCost)
VALUES (6, GETDATE(), 12.99);

GO
