CREATE_DW =  """
CREATE TABLE IF NOT EXISTS dimShipStatus(
	ShipStatusID INT NOT NULL AUTO_INCREMENT,
	ShipStatusName VARCHAR(50), 
    PRIMARY KEY(ShipStatusID)
);

CREATE TABLE IF NOT EXISTS dimFulfillment(
	FulfillmentID INT PRIMARY KEY,
	FulfillmentName VARCHAR(15) 
);

CREATE TABLE IF NOT EXISTS dimSalesChannel(
	SalesChannelID INT PRIMARY KEY,
	SalesChannelName VARCHAR(15) 
);

CREATE TABLE IF NOT EXISTS dimShipService(
    ShipServiceID INT PRIMARY KEY,
    ShipServiceName VARCHAR(15) 
);

CREATE TABLE IF NOT EXISTS dimProduct(
    ProductID INT PRIMARY KEY,
    SKU VARCHAR(50) UNIQUE,
    Style varchar(15),
    Category varchar(30),
    Size varchar(10),
    ASIN varchar (15)
);

CREATE TABLE IF NOT EXISTS dimCourierStatus(
    CourierStatusID INT PRIMARY KEY,
    CourierStatusName VARCHAR(15) 
);

CREATE TABLE IF NOT EXISTS dimCurrency(
    CurrencyID INT PRIMARY KEY,
    CurrencyName VARCHAR(15) 
);

CREATE TABLE IF NOT EXISTS dimPromotion(
    PromotionID INT PRIMARY KEY,
    PromotionName VARCHAR(50) 
);

CREATE TABLE IF NOT EXISTS dimFulfillmentBy(
    FulfillmentByID INT PRIMARY KEY,
    FulfillmentByName VARCHAR(15) 
);

CREATE TABLE IF NOT EXISTS dimShippingAddress(
    ShippingAddressID INT PRIMARY KEY,
    ShipCity VARCHAR(100) UNIQUE,
    ShipState VARCHAR(30) UNIQUE,
    ShipZipCode VARCHAR(10) UNIQUE,
    ShipCountry VARCHAR(10) 
);

create table if not exists dimDate(
    DateID date primary key,
    year int,
    semester int, 
    trimester int,
    month int,
    day int     
);

"""