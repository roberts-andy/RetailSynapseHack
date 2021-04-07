CREATE SCHEMA <schema_name>
GO

CREATE TABLE <schema_name>.Customer
	(
	 [Name] nvarchar(4000),
	 [Address] nvarchar(4000),
	 [City] nvarchar(4000),
	 [State] nvarchar(4000),
	 [PostalCode] bigint,
	 [Country] nvarchar(4000),
	 [PreferredStore] nvarchar(4000),
	 [RewardsPoints] bigint,
	 [CustomerRetailID] uniqueidentifier,
	 [img] nvarchar(4000),
	 [EmailId] nvarchar(4000)
	)
WITH
	(
	DISTRIBUTION = REPLICATE,
	 HEAP
	 -- CLUSTERED COLUMNSTORE INDEX
	)
GO


CREATE TABLE <schema_name>.Product
	(
	 [Name] nvarchar(4000),
	 [Cost] float,
	 [ListPrice] float,
	 [RetailProductID] uniqueidentifier
	)
WITH
	(
	DISTRIBUTION = REPLICATE,
	HEAP
	)
GO


CREATE TABLE <schema_name>.stores
	(
	 [StoreCode] bigint,
	 [Name] nvarchar(4000),
	 [Address] nvarchar(4000),
	 [City] nvarchar(4000),
	 [State] nvarchar(4000),
	 [PostalCode] bigint,
	 [Country] nvarchar(4000),
	 [Area] bigint,
	 [NumberofEmployees] bigint,
	 [StoreRetailID] uniqueidentifier,
	 [PhoneNumber] nvarchar(4000),
	 [Website] nvarchar(4000)
	)
WITH
	(
	DISTRIBUTION = replicate,
	 HEAP
	 -- CLUSTERED COLUMNSTORE INDEX
	)
GO

CREATE TABLE <schema_name>.TransactionDetail
	(
	 [CustomerRetailID] uniqueidentifier,
	 [TransactionHeaderID] uniqueidentifier,
	 [ProductRetailID] uniqueidentifier,
	 [Quantity] bigint,
	 [ListPrice] float,
	 [DiscountAmount] float,
	 [Tax] float,
	 [ShippingCost] float,
	 [TotalAmount] float
	)
WITH
	(
	DISTRIBUTION = HASH(TransactionHeaderID),
	 CLUSTERED COLUMNSTORE INDEX
	 -- HEAP
	)
GO


CREATE TABLE <schema_name>.TransactionHeader
	(
	 [TransactionHeaderID] uniqueidentifier,
	 [StoreRetailID] uniqueidentifier,
	 [CustomerRetailID] uniqueidentifier,
	 [Title] nvarchar(4000),
	 [Description] nvarchar(4000),
	 [Date] datetime2(0),
	 [TransactionType] nvarchar(4000),
	 [TransactionTotal] float,
	 [PaymentMethod] nvarchar(4000),
	 [Currency] nvarchar(4000)
	)
WITH
	(
	DISTRIBUTION = HASH(TransactionHeaderID),
	 CLUSTERED COLUMNSTORE INDEX
	 -- HEAP
	)
GO
